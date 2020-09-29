class AnimalBody(BasicBody):
    eyes = BasicBody.children_property(SimpleEye)
    mouth = BasicBody.child_property(SimpleMouth)
    skin = BasicBody.child_property(Exoskeleton)
    limbs = BasicBody.children_property(Limb)
    tail = BasicBody.child_property(Tail)
    flesh = BasicBody.child_property(Flesh, SoftFlesh)
    liquid = BasicBody.child_property(Jelly)

    default_name = 'body'
