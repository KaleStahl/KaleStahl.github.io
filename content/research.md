---
title: Research
menu: main
weight: 2
author: ""
---

I am currently supported with funding as an NSF Graduate Research Fellow.

My current research involves numerical methods for shape reconstruction in inverse scattering problems. In an inverse scattering problem, waves are scattered from an object, and the incident wave \(u^{in}\) and resulting wave \(u^{sc}\) are measured, with no a priori information about the scattering object. It is the goal of my work to use the information about the incident and scattered wave to determine characteristics about the unknown object. We can see a simple problem setup in the below image.

{{< figure src="/scattering_object_diagram.jpg" width="650">}}

There are many classes of methods proposed to solve this, but my work has been with sampling methods. In a sampling method, the domain is discretized and then an imaging functional is applied to each point. This functional returns a high value if the point is inside the object and a low value if it is outside. This allows us to numerically calculate the shape of the scattering object. In the below image, you can see the imaging method proposed in 1. compared to many other proposed sampling methods when used on a periodic object.

{{< figure src="/reconstructions.png" width="650">}}

---

# Publications and Papers

## Publications in Referreed Journals
1. D.L. Nguyen, **K. Stahl**, and T. Truong. *A new sampling indicator function for stable imaging of periodic scattering media* in Inverse Problems, Volume 39, Number 6, May 9, 2023. 
Link: [https://iopscience.iop.org/article/10.1088/1361-6420/acce5f/meta](https://iopscience.iop.org/article/10.1088/1361-6420/acce5f/meta) 
arXiv: [https://arxiv.org/abs/2205.01206](https://arxiv.org/pdf/2205.01206)

## Expository Works
**Undergraduate Honors Thesis**: *"Additional Proofs to Kirsch and Grinberg's 'The Factorization Method for Inverse Problems'"* [[pdf]](/files/Factorization%20Method.pdf)
### Lecture Notes
- Lecture Notes on Sobolev Inequalities [[pdf]](/files/GMT%20Lecture.pdf)
- Lecture Notes on Bipolar Green's Functions (in progress)