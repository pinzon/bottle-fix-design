import cadquery as cq

limit_height = 50  # mm
limit_width = 200  # mm
limit_depth = 150  # mm
base_height = 6  # mm
barrier_width = 4  # mm


def make_base():
    return (
        cq.Workplane("front")
        .box(limit_depth, limit_width, limit_height)
        .faces("+Z")
        .shell(base_height, "intersection")
    )


def make_barriers():
    return cq.Workplane("front").box(barrier_width, limit_width, limit_height)


def make_organizer():
    return make_base().union(make_barriers())


result = make_organizer()
