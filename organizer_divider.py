import cadquery as cq

height = 30
pts = [
    (0, 0),
    (0, 140),
    (4, 140),
    (4, 72),
    (70, 72),
    (70, 68),
    (4, 68),
    (4, 0),
]
piece = cq.Workplane("front").polyline(pts).close().extrude(height)
