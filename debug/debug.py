from fontTools.ttLib import TTFont

if __name__ == '__main__':
    font = TTFont('../reframework/fonts/NotoSansJP-Regular.otf')
    cmap = font['cmap'].getcmap(3, 1).cmap
    # for codepoint in sorted(cmap.keys()):
    #     print(f"U+{codepoint:04X} -> glyph {cmap[codepoint]}")
    print(f"U+{sorted(cmap.keys())[0]:04X}")
    print(f"U+{sorted(cmap.keys())[-1]:04X}")
