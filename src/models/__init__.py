"""Models to generate.

* encounters
* events
* fng
* generator_models
* history
* minerals
* name
* person
* planet
* redlands
* scales
* universe
* v5
* world

----

* models.model.Model - Base model.
  * models.complex_model.ComplexModel - Model with children.
    Used in: storm
  * models.data_item.DataItem
    Used in: and_why, dndspeak
  * models.deck.Deck - Model for cards deck.
    [UNUSED] [UNTESTED]
  * models.descriptive_model.DescriptiveModel - Model with description.
    [UNTESTED]
    Used in: fng
    * models.descriptive_model.ListDescriptiveModel - Model with description from list. 
      [UNUSED] [UNTESTED]
  * models.generated_model.GeneratedModel - Model with factory.
    Used in: fng
  * models.markov.MarkovUnit - Markov chain unit model.
    [UNTESTED]
    Used in: markov
  * models.markov.MarkovChain - Markov chain model.
    [UNTESTED]
    Used in: markov
  * models.name_block.NameBlock
    Used in: fng
  * models.name_item.NameItem
    Used in: fng
  * models.named_model.NamedModel - Model with name.
    Used in: nested, storm
    * models.nested_model.NestedModel - Model with name, parent and children.
      Used in: nested
  * models.point.Point - Model with x and y.
    [UNUSED] [UNTESTED]
  * models.preparable_model.PreparableModel - Preparable model.
    * models.name_model.Name - Base name model.
      [UNTESTED]
      Used in: text_factory
  * models.slotted.SlotItem - Model with slots. [UNTESTED]
    Used in: and_why
  * models.slotted.Slotted - Container with slots. [UNTESTED]
    Used in: and_why
* models.roll.Roll
  Used in: DiceFactory
  [UNTESTED]
"""
