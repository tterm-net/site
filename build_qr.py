#!/usr/bin/env python3
"""
build_qr.py — regenerate the donation QR codes.

The addresses are long enough that nobody will retype them, so the codes are
the primary way to pay from a phone. They are generated once into static SVG
files: the page stays a plain static site and never calls out to somebody
else's QR service with our wallet addresses.

Every file is parsed as XML before it is written. An earlier version painted
the modules by injecting a second `fill` attribute next to the one the library
already emits — valid-looking text, but a duplicate attribute, which browsers
reject outright and render as a broken image.
"""
from __future__ import annotations

import io
import pathlib
import re
import xml.etree.ElementTree as ET

import qrcode
import qrcode.image.svg

#: Dark modules on the white plate the page draws behind them.
MODULE = "#0d0e11"

ADDRESSES = {
    "trc20": "TPv5SQVhjczDR3fBPvGKBu9Ekn8gcziQTX",
    "erc20": "0xBc0B9cB860A6c789F7cB13DC59E6b5cf12Ab1fa0",
}

OUT = pathlib.Path(__file__).parent / "assets"


def render(data: str) -> str:
    qr = qrcode.QRCode(
        box_size=10,
        border=2,               # the quiet zone is part of the spec
        error_correction=qrcode.constants.ERROR_CORRECT_M,
    )
    qr.add_data(data)
    qr.make(fit=True)

    buf = io.BytesIO()
    qr.make_image(image_factory=qrcode.image.svg.SvgPathImage).save(buf)
    svg = buf.getvalue().decode()

    svg = svg.replace("<?xml version='1.0' encoding='UTF-8'?>\n", "")
    # Millimetre dimensions would pin the size; the page scales it instead.
    svg = re.sub(r'\swidth="[^"]+"\s+height="[^"]+"', "", svg, count=1)
    # Recolour the existing attribute rather than adding a second one.
    svg = svg.replace('fill="#000000"', f'fill="{MODULE}"')
    return svg


def main() -> None:
    for name, address in ADDRESSES.items():
        svg = render(address)

        ET.fromstring(svg)                      # refuses to ship broken XML
        fills = re.findall(r'fill="[^"]*"', svg)
        assert len(set(fills)) == 1 and fills[0] == f'fill="{MODULE}"', fills

        (OUT / f"qr-{name}.svg").write_text(svg, encoding="utf-8")
        print(f"  qr-{name}.svg  ({len(svg) // 1024} KB, {len(fills)} module path)")


if __name__ == "__main__":
    main()
