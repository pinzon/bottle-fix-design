import cadquery as cq


height = 10
pts = [
    (0, 0),
    (0, 8),
    (2,8),
    (2,2),
    (6,2),
    (6,0),
]
holder_radius = 2.7/2
l = cq.Workplane("front").polyline(pts).close().extrude(height)
l=l.faces("<X").workplane().center(-3.35,2).circle(holder_radius).extrude(5.5)

