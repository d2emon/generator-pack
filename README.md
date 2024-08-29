# Generator-Pack

Generators pack for RPG

## Inspirations

* http://www.fantasynamegenerators.com
* http://www.generatorland.com
* http://orteil.dashnet.org/nested

## Philosophy

* A game about:
  * **The beauty of emergent complexity,** on the familiar examples `(emergent complexity)`
  * **The challenge of understanding interdependent systems that form a whole** `(interdependent systems)`
  * **The experience of having an idea, developing it, and making it real** `(planning)`
  * **The interplay between conscious action and organic reaction** `(all = organisms)`
* Interaction through powerful but simple tools `(making a world with parameters)`
* Clear means to see patterns of behavior and consequences of one’s actions - in the small and in the large `(clarity)`
* Planning & collaboration is the way humans work to achieve great things `(planning)` `(collaboration)`
* Objects don't exist until they are called `(lazy computing)`

## Decisions

* Generate large continuous regions with several million inhabitants `(vastness)` `(multi-scale)`
* Overlayed time-scales: Daily and yearly activities happen at a similar pace `(multi-scale)`
* Persistent and unique individuals (people & businesses) `(diverse individuals)`

## Implementation Philosophy

* Develop systems from first principles, with complex behaviors emerging from simple microscopic interactions `(emergence)`
* Solve problems generally, do not restrict thinking in specialized problem instances `(actual problem)`
* Be brave to do things in new ways, where necessary `(radicality)`

## Implementation Decisions

* Use Python as the main programming language for high performance and a strong type system to rely on
* Use an actor-based model for isolation, dynamic dispatch and simple parallelization and networking

## Parts

* [Base Generator](generator/README.md) (0% alpha)
* Sample Generators
  * [Fantasy Name Generator](generator/fng/README.md) (0% alpha)
  * [Demographics](generator/demographics/README.md) (0% alpha)
  * [Timeline](generator/timeline/README.md) (0% alpha)

## Gameplay & Skills

* "Generating something"

## Contents

* config
* data
* database
* factories
* genesys
* helpers
* models
* rpg
* tests
* utils

## Steps

1. Run all **tests**
2. Run selected **genesys**
3. **Genesys** select factory from **factories**
  1. **Factory** uses **config**
  2. **Factory** loads **data**
  3. **Factory** use **helpers** to generate data
  4. **Factory** use **utils** to generate data
  5. **Factory** save generated data to model from **models**

* database
* rpg
