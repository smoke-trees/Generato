# Generato


We created a smart power distribution system, where all energy measuring smart meters are connected in a clustered architecture. This forms a better way to extract and aggregate information from the meters. The meter's reading is updated on an app for the user's understanding.

We implemented a Time Step Autoregression model to learn the energy consumption pattern  of each meter in the cluster, so that we can project how much power the meter has read based on the previous values, and if there is a huge difference between the projected and actual value, then an alarm is raised, indicating a power theft, or a faulty appliance.

We also implemented a Reinforcement Learning model to predict the generators that can compensate the load of a faulty generator in the network. This can be done based on the data provided by our clustered architecture. This overcomes the cascading effects of generator failure, and automates load balancing of power in such a case.
