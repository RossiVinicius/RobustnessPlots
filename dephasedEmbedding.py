import numpy as np
from math_tools import FindStateConeFacets, FindEffectConeFacets
from simplexEmbedding import DefineAccessibleGPTFragment, SimplicialConeEmbedding

def DephasedEmbedding(states, effects, unit, axis, debug=False):
    """
    Constructs a noncontextual ontological model for the (possibly dephased) GPT fragment.
    Tests whether a simplex embedding exists given the GPT's states, effects, unit, and a dephasing basis.
    

    Parameters:
    states (np.ndarray): A numpy array of states.
    effects (np.ndarray): A numpy array of effects.
    unit (np.ndarray): The unit effect.
    axis (np.ndarray): A numpy array of special effects characterising the dephasing basis.
    debug (bool, optional): Flag to print debug information. Default is False.

    Returns:
    tuple: A tuple containing:
        - robustness (float): The robustness value.
        - ResponseFunction (np.ndarray): The response function matrix.
        - EpistemicStates (np.ndarray): The epistemic states matrix.
    """

    inclusion_S, projection_S, accessibleFragmentStates = DefineAccessibleGPTFragment(
        states
    )
    inclusion_E, projection_E, accessibleFragmentEffects = DefineAccessibleGPTFragment(
        effects
    )
#    accessibleFragmentUnit = projection_E @ unit
    accessibleFragmentAxis = projection_E @ axis

    H_S = FindStateConeFacets(accessibleFragmentStates)
    H_E = FindEffectConeFacets(accessibleFragmentEffects)

    # Bilinear form giving the Born rule in the accessible fragment:
    accessibleFragmentBornRule = inclusion_E.T @ inclusion_S
    dephasingMap = accessibleFragmentAxis @accessibleFragmentAxis.T@accessibleFragmentBornRule
    robustness, sigma = SimplicialConeEmbedding(
        H_S, H_E, accessibleFragmentBornRule, dephasingMap
    )
#
    # Trivial factorization of the matrix sigma:
#    alpha = H_S
#   beta = H_E @ sigma
#
#    tau_S = np.array(
#        [
#            alpha[i, :] * (accessibleFragmentUnit @ beta[:, i])
#            for i in range(alpha.shape[0])
#            if not np.isclose((accessibleFragmentUnit @ beta[:, i]), 0)
#        ]
#    )
#    tau_E = np.array(
#        [
#            beta[:, i] / (accessibleFragmentUnit @ beta[:, i])
#            for i in range(beta.shape[1])
#            if not np.isclose((accessibleFragmentUnit @ beta[:, i]), 0)
#        ]
#    ).T
#
#    ResponseFunction = tau_E.T @ inclusion_E.T @ effects
#    EpistemicStates = tau_S @ inclusion_S.T @ states
#
    return robustness#, sigma, dephasingMap, ResponseFunction, EpistemicStates