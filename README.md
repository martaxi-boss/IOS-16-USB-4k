# IOS-16-USB-4K

Read-only extraction and static-analysis archive of the original Debian package `IOS 16 USB 4K (2).deb`.

This repository is intentionally isolated from `martaxi-boss/MotionCam-iOS`. It exists only as a separate reference project for technical comparison and preservation.

## Original package

- Package: `com.if-she.cydia.vcam`
- Name: `VCam for Entertainment`
- Version: `3.1.6`
- Architecture: `iphoneos-arm64`
- Depends: `mobilesubstrate, firmware (>= 15.0)`
- Layout: rootless (`/var/jb/...`)

## Repository layout

- `original/` — untouched original `.deb`
- `package/DEBIAN/` — extracted Debian control metadata and maintainer scripts
- `package/rootfs/` — exact installed filesystem payload
- `package/raw-ar/` — raw members of the Debian archive (`debian-binary`, `control.tar.gz`, `data.tar.lzma`)
- `analysis/` — read-only static analysis outputs, manifests, hashes, Mach-O metadata, strings and disassembly

## Important

No source code is claimed to be recovered from the compiled dylib. The `analysis/` directory contains static reverse-engineering output only. The original package remains preserved byte-for-byte in `original/`.
