Observations
============
Observations are generated for each controlled car in the scene. The type of observation can be specified in the config file as 'raw', 'Q-LIDAR', or 'bitmap'. The step function in the environment returns an observation for each controlled car in the scene as a list. 

Raw
^^^
A copy of the the raw environment, giving agents full access to the scene, and all other objects in the scene. Using this observation type should be avoided, as duplicating the environment incurs a significant performance penalty.

Q-LIDAR
^^^^^^^
A representation based on features a autonomus vehicle might extract from LIDAR sensors, which is the relative distance to collideable objects in the scene. This is a numpy array of distances produced by a Featurizer. The density and range of the Q-LIDAR beams can be configured in the featurizer.

.. autoclass:: gym_urbandriving.utils.featurizer.Featurizer
   :members: featurize

Bitmap
^^^^^^
Returns a Numpy image array as generated by the visualizer, for vision-based control agents. Image is a top-down view of the intersection.
