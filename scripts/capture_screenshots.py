#!/usr/bin/env python3
from __future__ import annotations

import json
import struct
import shutil
import subprocess
import tempfile
import zlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "guides.json"
OUT = ROOT / "assets" / "screenshots"
CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
TIMEOUT_SECONDS = 25


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    guides = json.loads(DATA.read_text(encoding="utf-8"))["guides"]
    if not CHROME.exists():
        print("Google Chrome not found, generating source cards instead.")
        for guide in guides:
            make_fallback_card(guide)
        return

    for guide in guides:
        target = OUT / f"{guide['slug']}.png"
        if target.exists() and target.stat().st_size > 10_000:
            print(f"skip {guide['slug']}", flush=True)
            continue
        ok = capture(guide["hero_url"], target)
        if ok:
            normalize(target)
            print(f"captured {guide['slug']}", flush=True)
        else:
            make_fallback_card(guide)
            print(f"fallback {guide['slug']}", flush=True)


def capture(url: str, target: Path) -> bool:
    with tempfile.TemporaryDirectory(prefix="awesome-practical-cn-chrome-") as tmp:
        cmd = [
            str(CHROME),
            "--headless=new",
            "--disable-gpu",
            "--disable-dev-shm-usage",
            "--no-first-run",
            "--no-default-browser-check",
            "--hide-scrollbars",
            "--window-size=1440,1000",
            f"--user-data-dir={tmp}",
            f"--screenshot={target}",
            url,
        ]
        try:
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=TIMEOUT_SECONDS)
        except subprocess.TimeoutExpired:
            return False
        return result.returncode == 0 and target.exists() and target.stat().st_size > 10_000


def normalize(path: Path) -> None:
    shutil.which("sips")
    if shutil.which("sips"):
        subprocess.run(["sips", "-Z", "1200", str(path)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def make_fallback_card(guide: dict) -> None:
    target = OUT / f"{guide['slug']}.png"
    colors = ["#2563eb", "#16a34a", "#9333ea", "#ea580c", "#0891b2", "#dc2626"]
    color = colors[sum(ord(c) for c in guide["slug"]) % len(colors)]
    write_simple_png(target, color)


def write_simple_png(path: Path, accent: str) -> None:
    width, height = 1200, 760
    bg = hex_to_rgb("#f8fafc")
    card = hex_to_rgb("#ffffff")
    border = hex_to_rgb("#dbe4ef")
    accent_rgb = hex_to_rgb(accent)
    rows = []
    for y in range(height):
        row = bytearray()
        for x in range(width):
            pixel = bg
            if 70 <= x <= 1130 and 80 <= y <= 680:
                pixel = card
            if (70 <= x <= 1130 and y in {80, 81, 679, 680}) or (80 <= y <= 680 and x in {70, 71, 1129, 1130}):
                pixel = border
            if (x - 135) ** 2 + (y - 145) ** 2 <= 34 ** 2:
                pixel = accent_rgb
            if 190 <= x <= 1000 and 130 <= y <= 170:
                pixel = (15, 23, 42)
            if 100 <= x <= 820 and 292 <= y <= 310:
                pixel = (51, 65, 85)
            if 100 <= x <= 1080 and 350 <= y <= 360:
                pixel = accent_rgb
            if 100 <= x <= 940 and 520 <= y <= 540:
                pixel = (100, 116, 139)
            row.extend(pixel)
        rows.append(bytes(row))
    raw = b"".join(b"\x00" + row for row in rows)
    png = b"\x89PNG\r\n\x1a\n"
    png += png_chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
    png += png_chunk(b"IDAT", zlib.compress(raw, 9))
    png += png_chunk(b"IEND", b"")
    path.write_bytes(png)


def png_chunk(kind: bytes, data: bytes) -> bytes:
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[index : index + 2], 16) for index in (0, 2, 4))


if __name__ == "__main__":
    main()
