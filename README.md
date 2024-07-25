# RobustnessPlots
Codes generating the plots in "Robustness of contextuality under different types of noise as quantifiers for parity-oblivious multiplexing tasks", available at https://arxiv.org/abs/2406.12773.

# Requirements
Requires functions available at https://github.com/pjcavalcanti/SimplexEmbeddingGPT. See README from that repository for further instructions.

# Functions
- Depolarised3to1PORAC(theta): Gives the sets of states, effects, the unit vector and the maximally mixed state for a 3-to-1 parity-oblivious multiplexing scenario implemented on a qubit, such that all states form an angle theta with respect to the Z axis of the Bloch sphere.
- Dephased3to1PORAC(theta,basis): Gives the esets of states, effects and the unit vector for a a 3-to-1 parity-oblivious multiplexing scenario implemented on a qubit, such that all states form an angle theta with respect to the Z axis of the Bloch sphere. Here the input basis is a collection of effects that characterise the dephasing axis.
- AnalyticalRobustness(x): Calculates the analytical robustness of depolarisation as a function of success rate as in Eq. 11 of the paper.
- Depolarised3to1PORACPlot(): Produces the plots in Fig. 3 of the paper.
- Dephased3to1PORACPlot(): Produces the plots in Fig. 4 of the paper.
- MinDephased3to1PORACPlot(): Produces the plots in Fig. 5 and 7 of the paper.
- ManyStates(n): Gives the set of states, effects, the unit vector and the maximally mixed state for the scenario considered in Appendix C1.
- PlotManyStates(): Produces the plot in Fig. 6 of the paper.

  # Acknowledgements
  We thank Bárbara Amaral for all the support and guidance on this manuscript, and Rafael Wagner, Giulio Camillo, and Anubhav Chaturvedi for the fruitful discussion. A.M.F. was supported by the São Paulo Research Foundation (FAPESP)  via Project Numbers 2022/05455-5 (FAS-Masters) and 2022/13208-8 (RIA-Research Internship Abroad), and from the Instituto Serrapilheira, Grant 2021/4. V.P.R. was supported by the Foundation for Polish Science (IRAP project, ICTQT, contract no. MAB/2018/5, co-financed by EU within Smart Growth Operational Programme). J.H.S. was supported by the National Science Centre, Poland (Opus project, Categorical Foundations of the Non-Classicality of Nature, Project
No. 2021/41/B/ST2/03149). R.D.B. and A.B.S. acknowledge support by the Digital Horizon Europe project FoQaCiA, Foundations of quantum computational advantage, GA No. 101070558, funded by the European Union, NSERC (Canada), and UKRI
(UK).
