import pdb
from models.source import Source
from models.sound import Sound
import repositories.source_repository as source_repository
import repositories.sound_repository as sound_repository

sound1 = Sound("Falcon Punch", "Cartoon Violence")
sound_repository.save(sound1)
sound2 = Sound("Energy Sword", "Sci-fi")
sound_repository.save(sound2)
sound3 = Sound("Sheikah Tower", "Fantasy")
sound_repository.save(sound3)

source1 = Source("Steak, celery, nuts, fan, voice", 5, sound1)
source_repository.save(source1)
source2 = Source("Glass bottle, running water, microwave", 3, sound2)
source_repository.save(source2)
source3 = Source("Keyboard, keys, breath, knives, mug", 5, sound3)
source_repository.save(source3)