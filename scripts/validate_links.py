#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "guides.json"
TIMEOUT = "4"


def main() -> None:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    failures: list[tuple[str, str, str]] = []
    warnings: list[tuple[str, str, str]] = []
    tasks: list[tuple[str, str, str]] = []
    for guide in payload["guides"]:
        links = [("hero", guide["hero_url"])] + [(name, url) for name, url, _ in guide["entries"]]
        for label, url in links:
            tasks.append((guide["slug"], label, url))
    with ThreadPoolExecutor(max_workers=16) as executor:
        future_map = {executor.submit(check, url): (slug, label, url) for slug, label, url in tasks}
        for future in as_completed(future_map):
            slug, label, url = future_map[future]
            state, reason = future.result()
            print(f"{state:4} {slug:28} {label:32} {url} {reason}", flush=True)
            if state == "FAIL":
                failures.append((slug, label, url))
            elif state == "WARN":
                warnings.append((slug, label, url))
    print(f"\nChecked {len(tasks)} links, warnings: {len(warnings)}, failures: {len(failures)}")
    if failures:
        sys.exit(1)


def check(url: str) -> tuple[str, str]:
    code, reason = curl(url, head=True)
    if code == "405" or code == "000":
        code, reason = curl(url, head=False)
    if code.isdigit() and (200 <= int(code) < 400 or int(code) in {401, 403, 429}):
        suffix = " reachable-gated" if int(code) in {401, 403, 429} else ""
        return "OK", f"{code}{suffix}"
    if code in {"000"}:
        return "WARN", f"{code} {reason}".strip()
    if code.isdigit() and int(code) in {404, 410}:
        return "FAIL", code
    return "WARN", f"{code} {reason}".strip()


def curl(url: str, head: bool) -> tuple[str, str]:
    cmd = [
        "curl",
        "-L",
        "-k",
        "--silent",
        "--show-error",
        "--max-time",
        TIMEOUT,
        "-A",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/126 Safari/537.36",
        "-o",
        "/dev/null",
        "-w",
        "%{http_code}",
    ]
    if head:
        cmd.append("--head")
    cmd.append(url)
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=int(TIMEOUT) + 2)
    except subprocess.TimeoutExpired:
        return "000", "timeout"
    return result.stdout.strip() or "000", result.stderr.strip().splitlines()[-1] if result.stderr.strip() else ""


if __name__ == "__main__":
    main()
