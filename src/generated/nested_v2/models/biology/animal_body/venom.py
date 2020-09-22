from generated.chemistry import elements, Proteins, Lipids, OrganicMatter


class Venom(OrganicMatter):
    class Factory(OrganicMatter.Factory):
        class ChildrenFactory(OrganicMatter.Factory.ChildrenFactory):
            def builders(self):
                yield Proteins
                yield Lipids.probable(40)
                yield elements['N'].probable(40)
                yield elements['Na'].probable(40)
                yield elements['Cl'].probable(40)
