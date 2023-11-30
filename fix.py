import cadquery as cq


height = 17
pts = [
    (0, 0),
    (0, 5),
    (2, 5),
    (2, 2),
    (4.2, 2),
    (4.2, 0),
]
holder_radius = 2.7 / 2
l = cq.Workplane("front").polyline(pts).close().extrude(height)
l = l.faces("<X").workplane().center(-3.35, 2).circle(holder_radius).extrude(5.5)
