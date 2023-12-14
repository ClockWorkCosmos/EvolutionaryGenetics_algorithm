# EvolutionaryGenetics_algorithm

Python; Artificial intelligence and machine learning

Evolve / learn obstacle avoidance behaviors; The top two agents that best avoid obstacles go on to produce a child offspring of mixed weights and thresholds from both parents.

Required modules / libraries:
  1. Sys
  2. Random
  3. Math
  4. Time
  5. Pygame

Network architecture:
  1. 3x Input units
  2. 3x Weighted connections
  3. 1x Hidden unit
  4. 2x Output units (turn randomly or move forward)

Policy (Supervised learning):
  1. If any of the input units are equal to or less than 0.3, the agent should turn, elsewise the agent should move forward.


- Parent A weights and threshold are equal to the weights and threshold of the agent with the highest score.
- Parent B weights and threshold are equal to the weights and threshold of the agent with a score quarter less than the highest scoring agent.
- Child offspring weights and threshold are equal to an even mix of Parent A and B weights and threshold, plus the mutation amount.
- Update generation.
  
Algorithm:
1. Randomize initial weight and threshold amounts between -0.99 and 0.99.
2. Input unit values are synonymous to the distance between the agent and the obstacle (0.00 - 0.99).
3. Compute hidden unit activation sum; Whereas activation sum is equal to the sum of each input unit multiplied by their associated weights.
4. If the activation sum is equal to or greater than the threshold amount, the hidden unit fires, else, it does not fire.
5. If the hidden unit fires, the agent will turn, else, the agent will move forward.
6. If the output does not equal the correct output, randomly adjust weights and threshold.
7. Repeat for each training episode.
