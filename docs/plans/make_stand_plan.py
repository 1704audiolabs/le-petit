"""Le Petit stand: one A3 sheet as SVG (views 1:5, detail 1:1), drawn with the building plan's helpers.

Four legs, two side bars and a middle bar, 6 mm bright round steel, silver-soldered; the legs screw
into M6 inserts glued into the box bottom, 22 mm from the outside faces (296 x 188 on the axes).
Run: python make_stand_plan.py  ->  stand-plan.svg
"""
from make_building_plan import OUT, Sheet, View, heading, f

DATE = "20.10.2026"
BW, BH, BD, DBL = 340, 530, 232, 22        # box (W x H x D), doubler in front
LEG, BAR_H, D = 300, 60, 6                 # visible leg, bar axis above the floor, rod Ø
E = 22                                     # leg axis from the box's outside faces
AX, AZ = BW - 2 * E, BD - 2 * E            # 296 x 188 on the axes
INSERT, THREAD = 13, 11                    # M6 glue-in insert length; thread = insert - 2


def frame(s):
    s.rect(10, 10, 400, 277, "o")
    x0, y0 = 283, 252
    s.rect(x0, y0, 127, 35, "o")
    s.text(x0 + 3, y0 + 8.5, "Le Petit", 6.2, cls="disp")
    s.text(x0 + 124, y0 + 5, "1704 Audio Labs", 1.7, "end", cls="mono")
    s.text(x0 + 27, y0 + 8.5, "stand", 2.4)
    s.text(x0 + 3, y0 + 13.5, "Ø6 bright round steel, silver-soldered · legs into M6 inserts in the box bottom", 1.8)
    s.text(x0 + 3, y0 + 17.5, "300 high: driver centre 715 above the floor, 830 overall", 1.8)
    s.text(x0 + 3, y0 + 23, "Stand", 2.5)
    s.line(x0, y0 + 25, x0 + 127, y0 + 25, "t")
    s.line(x0 + 72, y0 + 25, x0 + 72, y0 + 35, "t")
    s.line(x0 + 102, y0 + 25, x0 + 102, y0 + 35, "t")
    s.text(x0 + 3, y0 + 31, f"All dimensions in mm · {DATE}", 1.7)
    s.text(x0 + 75, y0 + 31, "Scale 1:5 (detail 1:1) @ A3", 1.7)
    s.text(x0 + 105, y0 + 31, "Stand sheet", 1.7)


def rod_v(v, u, w0, w1):        # a vertical rod, axis at u, from w0 down to w1
    v.rect(u - D / 2, w0, D, w1 - w0, "o")


def rod_h(v, u0, u1, w):        # a horizontal rod, axis at w, from u0 to u1
    v.rect(u0, w - D / 2, u1 - u0, D, "o")


def sheet():
    s = Sheet()
    floor = BH + LEG

    # FRONT VIEW: box outline, the doubler, the legs and the middle bar
    heading(s, 26, 25, "FRONT VIEW", "box as built, on the stand")
    v = View(s, 34, 37)
    v.rect(0, 0, BW, BH, "t")
    v.rect(20, BH - 300, 300, 300, "t")
    v.circle(170, 115, 47, "t")
    v.circle(170, BH - 150, 35, "t")
    for u in (E, BW - E):
        rod_v(v, u, BH, floor)
    rod_h(v, E, BW - E, floor - BAR_H)
    v.line(-30, floor, BW + 30, floor, "o")
    v.chain_h([E, BW - E], floor, 9, labels=[f"{AX} on the axes"])
    v.chain_h([0, E], 0, -5, labels=[f(E)])
    v.chain_v([0, BH, floor], BW, 10, labels=[f(BH), f"{LEG} visible"])
    v.chain_v([floor - BAR_H, floor], E, -12, labels=[f(BAR_H)])
    v.chain_v([115, floor], -14, 0, labels=["715 driver centre"])
    v.text(BW / 2, floor - BAR_H - 6, "middle bar", 1.6, "middle", fill="#5A5752")

    # SIDE VIEW: legs front and back, the side bar, the middle bar end-on
    heading(s, 128, 25, "SIDE VIEW", "from the right, front to the left")
    v = View(s, 134, 37)
    v.rect(DBL, 0, BD, BH, "t")
    v.rect(0, BH - 300, DBL, 300, "t")
    for u in (DBL + E, DBL + BD - E):
        rod_v(v, u, BH, floor)
    rod_h(v, DBL + E, DBL + BD - E, floor - BAR_H)
    v.circle(DBL + BD / 2, floor - BAR_H, D / 2, "o")
    v.line(-20, floor, DBL + BD + 30, floor, "o")
    v.chain_h([DBL + E, DBL + BD - E], floor, 9, labels=[f"{AZ} on the axes"])
    v.chain_h([0, DBL, DBL + BD], floor, 16, labels=[f(DBL), f(BD)])
    v.text(DBL + BD / 2, floor - BAR_H - 6, "side bar", 1.6, "middle", fill="#5A5752")

    # PLAN of the stand under the box (box footprint dashed)
    heading(s, 205, 25, "PLAN", "the stand from above, box footprint dashed")
    v = View(s, 215, 40, 0.3)
    v.rect(0, 0, BW, BD, "hd")
    for u in (E, BW - E):
        for w in (E, BD - E):
            v.circle(u, w, D / 2 + 1, "o")
        rod_v(v, u, E, BD - E)
    rod_h(v, E, BW - E, BD / 2)
    v.text(BW / 2, -4, "front", 1.6, "middle", fill="#5A5752")
    v.chain_h([0, E, BW - E, BW], BD, 7, labels=[f(E), f"{AX}", f(E)])
    v.chain_v([0, E, BD - E, BD], BW, 8, labels=[f(E), f"{AZ}", f(E)])
    v.text(BW / 2, BD / 2 - 4, "middle bar 296 axis · 290 cut", 1.5, "middle")
    v.text(BW / 2, BD / 2 + 8, "side bars 188 axis · 182 cut", 1.5, "middle")

    # DETAIL: leg top in the box bottom, 1:1
    heading(s, 205, 135, "DETAIL A  1:1", "leg into the glued-in M6 insert")
    v = View(s, 225, 148, 1.0)
    v.rect(0, 0, 50, 22, "cut")                         # box bottom panel, in section
    v.text(0, -2, "box bottom, 22 OSB, in section", 1.7)
    v.rect(25 - 4.25, 22 - INSERT - 3, 8.5, INSERT + 3, "w")    # bore Ø8–8.5, insert + 3 deep
    v.rect(25 - 5, 22 - INSERT, 10, INSERT, "o")              # insert
    v.rect(25 - 6, 22 - 1, 12, 1, "o")                        # flange, flush with the underside
    v.rect(25 - D / 2, 22 - THREAD, D, THREAD + 26, "o")      # leg: thread inside, rod below
    v.line(25, 22 - THREAD - 6, 25, 22 + 30, "c")
    # leaders ordered top to bottom so they don't cross
    s.leader(225 + 29.25, 148 + 22 - INSERT - 1.5, 290, 144, "bore Ø8–8.5, insert + 3 deep (≈16)", 1.7)
    s.leader(225 + 30, 148 + 22 - INSERT + 3, 290, 150, "M6 glue-in insert, Ø≈10 × 13, epoxy", 1.7)
    s.leader(225 + 28, 148 + 22 - THREAD + 6, 290, 156, f"thread M6 × {THREAD} (insert − 2)", 1.7)
    s.leader(225 + 31, 148 + 21.5, 290, 162, "flange flush with the underside", 1.7)
    s.leader(225 + 28, 148 + 40, 290, 168, "Ø6 leg, shoulder sits on the flange", 1.7)

    # CUT LIST + CUTTING PLAN + HARDWARE
    x, y = 26, 222
    s.text(x, y, "CUT LIST, PER STAND", 2.4)
    rows = (("4", "leg", f"{LEG + THREAD} = {LEG} visible + {THREAD} thread"),
            ("2", "side bar", "182 cut · 188 on the axes"),
            ("1", "middle bar", "290 cut · 296 on the axes"))
    for i, (q, n, l) in enumerate(rows):
        s.text(x, y + 5 + i * 3.6, q, 1.9)
        s.text(x + 6, y + 5 + i * 3.6, n, 1.9)
        s.text(x + 26, y + 5 + i * 3.6, l, 1.9)
    s.text(x, y + 19, "≈ 1.9 m per stand, ≈ 3.9 m for the pair", 1.8, fill="#3A3732")

    x, y = 110, 228
    s.text(x, y, "CUTTING PLAN, PAIR: 3 BARS × 1500", 2.4)
    k = 0.11
    for i, (name, cuts) in enumerate((("A", (315, 315, 315, 315, 188)), ("B", (315, 315, 315, 315, 188)),
                                      ("C", (188, 188, 296, 296)))):
        yy = y + 4 + i * 7
        s.text(x, yy + 2.6, name, 1.9)
        s.rect(x + 4, yy, 1500 * k, 3.2, "t")
        u = 0
        for c in cuts:
            s.rect(x + 4 + u * k, yy, c * k, 3.2, "o")
            s.text(x + 4 + (u + c / 2) * k, yy + 2.4, f(c), 1.4, "middle")
            u += c + 3
        s.text(x + 4 + 1500 * k + 2, yy + 2.4, f"rest ≈ {1500 - u}", 1.5)
    s.text(x, y + 26, "legs 315 (15 thread), 311 for a 13 insert · bars cut at axis length, trimmed to 182 / 290 to fit · 3 mm kerf", 1.7, fill="#3A3732")

    x, y = 283, 186
    s.text(x, y, "HARDWARE, PAIR", 2.4)
    for i, (q, t) in enumerate((("3", "bright round steel Ø6, 1500 (not hot-rolled)"),
                                ("8", "M6 glue-in inserts Ø≈10 × 13 (buy 12)"),
                                ("", "2-part epoxy · silver solder + flux · M6 die"))):
        s.text(x, y + 5 + i * 3.6, q, 1.9)
        s.text(x + 6, y + 5 + i * 3.6, t, 1.9)
    s.text(x, y + 20, "CHECK BEFORE YOU DRILL", 2.4)
    for i, t in enumerate(("Cut the four legs of a stand as one bundle.",
                           "Take the hole positions from the finished stand.",
                           "At 22 the bore sits in the inner corner: drill press +",
                           "centre drill, or go to 30 (280 × 172 on the axes).")):
        s.text(x, y + 25 + i * 3.6, t, 1.8)
    frame(s)
    return s


if __name__ == "__main__":
    p = OUT / "stand-plan.svg"
    p.write_text(sheet().svg())
    print("wrote", p.name)
