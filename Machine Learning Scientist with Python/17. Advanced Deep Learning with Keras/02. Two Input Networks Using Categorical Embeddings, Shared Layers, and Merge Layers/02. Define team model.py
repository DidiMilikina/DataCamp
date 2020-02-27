'''
Define team model
The team strength lookup has three components: an input, an embedding layer, and a flatten layer that creates the output.

If you wrap these three layers in a model with an input and output, you can re-use that stack of three layers at multiple places.

Note again that the weights for all three layers will be shared everywhere we use them.

Instructions
100 XP
Create a 1D input layer for the team ID (which will be an integer). Be sure to set the correct input shape!
Pass this input to the team strength lookup layer you created previously.
Flatten the output of the team strength lookup.
Create a model that uses the 1D input as input and flattened team strength as output.
'''
SOLUTION

# Imports
from keras.layers import Input, Embedding, Flatten
from keras.models import Model

# Create an input layer for the team ID
teamid_in = Input(shape=(1,))

# Lookup the input in the team strength embedding layer
strength_lookup = team_lookup(teamid_in)

# Flatten the output
strength_lookup_flat = Flatten()(strength_lookup)

# Combine the operations into a single, re-usable model
team_strength_model = Model(teamid_in, strength_lookup_flat, name='Team-Strength-Model')