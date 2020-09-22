from generated.chemistry import elements, Matter


class ClamShell(Matter):
    class Factory(Matter.Factory):
        class ChildrenFactory(Matter.Factory.ChildrenFactory):
            def builders(self):
                yield elements['Ca']
