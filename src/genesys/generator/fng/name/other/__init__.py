from .album import AlbumGenerator, Album
from .band import BandGenerator, Band

"""
										<li><a href="http://www.fantasynamegenerators.com/afterlife-names.php">Afterlife Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/alliance-names.php">Alliance Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/animal-group-names.php">Animal Group Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/apocalypse-names.php">Apocalypse Names</a></li>
										<li style="font-size: 100%; padding: 3px 0.5%;">Armor Names &gt;
											<ol>
												<li><a href="http://www.fantasynamegenerators.com/belt-names.php">Belts</a></li>
												<li><a href="http://www.fantasynamegenerators.com/boots-names.php">Boots</a></li>
												<li><a href="http://www.fantasynamegenerators.com/vambrace-names.php">Bracers</a></li>
												<li><a href="http://www.fantasynamegenerators.com/chest-names.php">Chests</a></li>
												<li><a href="http://www.fantasynamegenerators.com/cloak-names.php">Cloaks</a></li>
												<li><a href="http://www.fantasynamegenerators.com/gauntlet-names.php">Gloves &amp; Gauntlets</a></li>
												<li><a href="http://www.fantasynamegenerators.com/helmet-names.php">Helmets</a></li>
												<li><a href="http://www.fantasynamegenerators.com/leg-names.php">Legs</a></li>
												<li><a href="http://www.fantasynamegenerators.com/pauldron-names.php">Pauldrons</a></li>
												<li><a href="http://www.fantasynamegenerators.com/shield-names.php">Shields</a></li>
											</ol>
										</li>
										<li><a href="http://www.fantasynamegenerators.com/army-names.php">Army Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/dwarf-army-names.php">Army Names (Dwarf) <span class="red">- New!</span></a></li>
										<li><a href="http://www.fantasynamegenerators.com/artifact-names.php">Artifact Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/artwork-names.php">Artwork Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/attack-move-names.php">Attack Move Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/anime-attack-names.php">Attack Names (Anime)</a></li>
										<li><a href="http://www.fantasynamegenerators.com/award-names.php">Award Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/battle-names.php">Battle Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/board-game-names.php">Board Game Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/book-title-generator.php">Book Titles</a></li>
										<li><a href="http://www.fantasynamegenerators.com/bouquet-names.php">Bouquet Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/boxer-names.php">Boxer Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/brand-names.php">Brand Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/bug-species-names.php">Bug Species Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/candy-names.php">Candy Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/chivalric-order-names.php">Chivalric Order Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/clothing-brand-names.php">Clothing Brand Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/clown-names.php">Clown Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/color-names.php">Color Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/computer-virus-names.php">Computer Virus Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/console-names.php">Console Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/constellation-names.php">Constellation Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/council-names.php">Council Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/crop-names.php">Crop Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/currency-names.php">Currency Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/curse-names.php">Curse Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/dance-names.php">Dance Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/date-names.php">Date Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/disease-names.php">Disease Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/magical-disease-names.php">Disease (Magical) Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/scientific-disease-names.php">Disease (Scientific) Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/dinosaur-names.php">Dinosaur Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/drink-names.php">Drink Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/drug-names.php">Drug Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/enchantment-names.php">Enchantment Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/gear-enchantment-names.php">Enchanted Gear Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/energy-types.php">Energy Types</a></li>
										<li><a href="http://www.fantasynamegenerators.com/epithet-generator.php">Epithets</a></li>
										<li><a href="http://www.fantasynamegenerators.com/evil-group-names.php">Evil Organizations</a></li>
										<li><a href="http://www.fantasynamegenerators.com/magical-plant-names.php">Fantasy Plant Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/magical-tree-names.php">Fantasy Tree Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/profession-names.php">Fantasy Profession Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/food-names.php">Food Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/fantasy-food-names.php">Food Names (Fantasy)</a></li>
										<li><a href="http://www.fantasynamegenerators.com/fruit-vegetable-names.php">Fruit &amp; Veg. Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/fungi_names.php">Fungus Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/galaxy-names.php">Galaxy Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/game-engine-names.php">Game Engine Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/game-soundtrack-names.php">Game Soundtrack Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/gang-names.php">Gang / Clan Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/gem-mineral-names.php">Gemstone/Mineral</a></li>
										<li><a href="http://www.fantasynamegenerators.com/graffiti-tags.php">Graffiti Tags</a></li>
										<li><a href="http://www.fantasynamegenerators.com/guild_names.php">Guild / Clan Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/hacker-names.php">Hacker Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/heist-names.php">Heist Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/herb-names.php">Herb &amp; Spice Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/holiday-names.php">Holiday Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/holy-book-names.php">Holy Book Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/human-species-names.php">Human Species Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/instrument-names.php">Instrument Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/invention-names.php">Invention Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/jewelry-names.php">Jewelry Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/language-names.php">Language Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/love-nicknames.php">Love nicknames</a></li>
										<li><a href="http://www.fantasynamegenerators.com/magazine-names.php">Magazine Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/magic-types.php">Magic Types</a></li>
										<li><a href="http://www.fantasynamegenerators.com/martial-arts-names.php">Martial Arts Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/mascot-names.php">Mascot Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/material-names.php">Material Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/medicine-names.php">Medicine Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/metal_names.php">Metal/Element Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/military-division-names.php">Military Division Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/military-honor-names.php">Military Honor Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/military-operation-names.php">Military Operation Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/military-rank-names.php">Military Rank Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/mobster-names.php">Mobster Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/molecule-names.php">Molecule Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/motorcycle-club-names.php">Motorcycle Clubs</a></li>
										<li><a href="http://www.fantasynamegenerators.com/motorsport-race-names.php">Motorsport Races</a></li>
										<li><a href="http://www.fantasynamegenerators.com/album-names.php">Music Album Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/band-names.php">Music Band Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/musician-names.php">Musician Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/mutant-plant-names.php">Mutant Plant Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/natural-disaster-names.php">Natural Disaster Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/newspaper-names.php">Newspaper Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/nicknames.php">Nicknames</a></li>
										<li><a href="http://www.fantasynamegenerators.com/noble-house-names.php">Noble House Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/pirate-crew-names.php">Pirate Crew Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/plague-names.php">Plague Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/tree_names.php">Plant and Tree Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/class-names.php">Player Class &amp; NPC Types</a></li>
										<li><a href="http://www.fantasynamegenerators.com/poison-names.php">Poison Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/political-party-names.php">Political Party Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/post-apocalyptic-society-names.php">Post-Apocalyptic Society</a></li>
										<li><a href="http://www.fantasynamegenerators.com/potion-names.php">Potion Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/racer-names.php">Racer Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/railway-names.php">Railway Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/rank-names.php">Rank Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/religion-names.php">Religion Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/satellite-names.php">Satellite Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/bird_names.php">Scientific Bird Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/scientific-creature-names.php">Scientific Creature Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/plant_names.php">Scientific Plant Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/magic-school-book-names.php">School Book Names (Magic)</a></li>
										<li><a href="http://www.fantasynamegenerators.com/siege-engine-names.php">Siege Engine Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/software-names.php">Software Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/song-title-generator.php">Song Titles</a></li>
										<li><a href="http://www.fantasynamegenerators.com/space-fleet-names.php">Space Fleet Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/spell-names.php">Spell Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/sport-names.php">Sport Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/sports-team-names.php">Sports Team Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/squad-names.php">Squad Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/steampunk-walker-names.php">Steampunk Walker Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/superpowers.php">Superpowers</a></li>
										<li><a href="http://www.fantasynamegenerators.com/teleportation-names.php">Teleportation Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/theme-park-rides.php">Theme Park Ride Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/throne-names.php">Throne Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/time-period-names.php">Time Period Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/title-names.php">Title Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/tool-nicknames.php">Tool Nicknames</a></li>
										<li><a href="http://www.fantasynamegenerators.com/treaty-names.php">Treaty Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/tribal-names.php">Tribal Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/tribe-names.php">Tribe Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/username-generator.php">Usernames</a></li>
										<li style="font-size: 100%; padding: 3px 0.5%;">Vehicle Names &gt;
											<ol>
												<li><a href="http://www.fantasynamegenerators.com/airplane-names.php">Airplane Names</a></li>
												<li><a href="http://www.fantasynamegenerators.com/airship-names.php">Airship Names</a></li>
												<li><a href="http://www.fantasynamegenerators.com/car-names.php">Car Names</a></li>
												<li><a href="http://www.fantasynamegenerators.com/helicopter-names.php">Helicopter Names</a></li>
												<li><a href="http://www.fantasynamegenerators.com/military-vehicle-names.php">Military Vehicle Names</a></li>
												<li><a href="http://www.fantasynamegenerators.com/pirate-ship-names.php">Pirate Ship Names</a></li>
												<li><a href="http://www.fantasynamegenerators.com/ship-names.php">Ship Names</a></li>
												<li><a href="http://www.fantasynamegenerators.com/spaceship-names.php">Spaceship Names</a></li>
												<li><a href="http://www.fantasynamegenerators.com/submarine-names.php">Submarine Names</a></li>
												<li><a href="http://www.fantasynamegenerators.com/tank-names.php">Tank Names</a></li>
												<li><a href="http://www.fantasynamegenerators.com/vehicle-names.php">Vehicle Names</a></li>
											</ol>
										</li>
										<li><a href="http://www.fantasynamegenerators.com/video-game-names.php">Video Game Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/vocal-group-names.php">Vocal Group Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/weapon-abilities.php">Weapon Abilities</a></li>
										<li style="font-size: 100%; padding: 3px 0.5%;">Weapon Names &gt;
											<ol>
												<li><a href="http://www.fantasynamegenerators.com/battle-axe-names.php">Battle Axe Names</a></li>
												<li><a href="http://www.fantasynamegenerators.com/bomb-missile-names.php">Bombs &amp; Missiles</a></li>
												<li><a href="http://www.fantasynamegenerators.com/bow-names.php">Bows &amp; Crossbows</a></li>
												<li><a href="http://www.fantasynamegenerators.com/claw-weapon-names.php">Claws</a></li>
												<li><a href="http://www.fantasynamegenerators.com/dagger-names.php">Daggers</a></li>
												<li><a href="http://www.fantasynamegenerators.com/dual-wield-names.php">Dual Wielding</a></li>
												<li><a href="http://www.fantasynamegenerators.com/fist-weapon-names.php">Fist Weapons</a></li>
												<li><a href="http://www.fantasynamegenerators.com/flail-names.php">Flails &amp; Maces</a></li>
												<li><a href="http://www.fantasynamegenerators.com/magic-book-names.php">Magic Books</a></li>
												<li><a href="http://www.fantasynamegenerators.com/magic-weapon-names.php">Magic Weapons</a></li>
												<li><a href="http://www.fantasynamegenerators.com/pistol-names.php">Pistols</a></li>
												<li><a href="http://www.fantasynamegenerators.com/rifle-names.php">Rifles</a></li>
												<li><a href="http://www.fantasynamegenerators.com/sci-fi-gun-names.php">Sci-Fi Guns</a></li>
												<li><a href="http://www.fantasynamegenerators.com/shotgun-names.php">Shotguns</a></li>
												<li><a href="http://www.fantasynamegenerators.com/spear-names.php">Spears &amp; Halberds</a></li>
												<li><a href="http://www.fantasynamegenerators.com/staff-names.php">Staves</a></li>
												<li><a href="http://www.fantasynamegenerators.com/sword-names.php">Swords</a></li>
												<li><a href="http://www.fantasynamegenerators.com/throwing-weapon-names.php">Throwing Weapons</a></li>
												<li><a href="http://www.fantasynamegenerators.com/war-hammer-names.php">War Hammers</a></li>
												<li><a href="http://www.fantasynamegenerators.com/scythe-names.php">War Scythes</a></li>
												<li><a href="http://www.fantasynamegenerators.com/whip-names.php">Whips &amp; Lassos</a></li>
											</ol>
										</li>
										<li><a href="http://www.fantasynamegenerators.com/web-series-names.php">Web Series</a></li>
										<li><a href="http://www.fantasynamegenerators.com/wine-names.php">Wine Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/wrestler-names.php">Wrestler Names</a></li>
										<li><a href="http://www.fantasynamegenerators.com/wrestling-move-names.php">Wrestling Move Names</a></li>
"""