# quadcopter-gazebo-model-enhanced
Enhanced Gazebo model of a quadcopter enabling the creation of world with multiple instances.

This project is an enhanced quadcopter model for Gazebo.
It's an updated version of the example Gazebo quadcopter model, located in: 
/usr/share/gazebo-5.3/worlds/quad_rotor_demo.world

The use case for this model was multi-robot collaboration/swarms.
So wonder2d wanted to have a world where they could ideally spawn multiple instances of a single model.
However there were difficulties in achieving this in Gazebo.
So a different approach was taken, where a template model file with a placeholder model name was created.
When wanting to have multiple quads in the world, a simple Python script is used to copy the quad model template and update the model name placeholder.
Then in the Gazebo world file, they could simply include the individual quad models.
This method worked really well.

Also, the preference was for the models developed to be in the local workspace directory.
The standard Gazebo setup.sh script was copied and the model paths added.
So there's a boot2292.sh script that runs the custom setup script, then boots a world with three quads.
From there, the user can run controller applications which interface with the Gazebo world and control the quads.

To run, update your paths in modelDev/gz_setup.sh, then source boot2292.sh.
If you want to change the number o