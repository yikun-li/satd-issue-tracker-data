# SATD Dataset in Issue Tracking Systems

##### Authors: Yikun Li, Mohamed Soliman, Paris Avgeriou

## Description of This Study

Technical debt is a metaphor indicating sub-optimal solutions implemented for short-term benefits by sacrificing the long-term maintainability and evolvability of software. 
A special type of technical debt is explicitly admitted by software engineers (e.g. using a TODO comment); this is called **Self-Admitted Technical Debt** or **SATD**.
Most work on automatically identifying SATD focuses on source code comments.
In addition to source code comments, issue tracking systems have shown to be another rich source of SATD, but there are no approaches specifically for automatically identifying SATD in issues.
In this paper, we first create a training dataset by collecting and manually analyzing 4,200 issues (that break down to 23,180 sections of issues) from seven open-source projects (i.e., Camel, Chromium, Gerrit, Hadoop, HBase, Impala, and Thrift) using two popular issue tracking systems (i.e., Jira and Google Monorail).
We then propose and optimize an approach for automatically identifying SATD in issue tracking systems using machine learning.
Our findings indicate that: 1) our approach outperforms baseline approaches by a wide margin with regard to the F1-score; 2) transferring knowledge from suitable datasets can improve the predictive performance of our approach; 3) extracted SATD keywords are intuitive and potentially indicating types and indicators of SATD; 4) projects using different issue tracking systems have less common SATD keywords compared to projects using the same issue tracking system; 5) a small amount of training data is needed to achieve good accuracy.


## Structure of the Replication Package

The package contains a **trained SATD detector model** that can be used for further research and analysis. Additionally, we have assembled a replication package that includes a **dataset of SATD from issue tracking systems**. This dataset contains 23,180 issue sections (including 3,277 SATD issue sections) from seven large open-source projects across two ecosystems: Apache and Google. We define each part of an issue, such as summary, description, or comment, as an issue section. The number of different types/indicators of SATD is shown below:

| Type of SATD       | Indicator                                             | Definition                                                                                                                                                                                            | Number |
|--------------------|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Architecture debt  | Violation of modularity                               | Because shortcuts were taken, multiple modules became inter-dependent, while they should be independent.                                                                                              | 46     |
|                    | Using obsolete technology                             | Architecturally-significant technology has become obsolete.                                                                                                                                           | 41     |
| Build debt         | Over- or under-declared dependencies                  | Under-declared dependencies: dependencies in upstream libraries are not declared and rely on dependencies in lower level libraries. Over-declared dependencies: unneeded dependencies are declared.   | 25     |
|                    | Poor deployment practice                              | The quality of deployment is low that compile flags or build targets are not well organized.                                                                                                          | 39     |
| Code debt          | Complex code                                          | Code has accidental complexity and requires extra refactoring action to reduce this complexity.                                                                                                       | 30     |
|                    | Dead code                                             | Code is no longer used and needs to be removed.                                                                                                                                                       | 121    |
|                    | Duplicated code                                       | Code that occurs more than once instead of as a single reusable function.                                                                                                                             | 40     |
|                    | Low-quality code                                      | Code quality is low, for example because it is unreadable, inconsistent, or violating coding conventions.                                                                                             | 856    |
|                    | Multi-thread correctness                              | Thread-safe code is not correct and may potentially result in synchronization problems or efficiency problems.                                                                                        | 40     |
|                    | Slow algorithm                                        | A non-optimal algorithm is utilized that runs slowly.                                                                                                                                                 | 159    |
| Defect debt        | Uncorrected known defects                             | Defects are found by developers but ignored or deferred to be fixed.                                                                                                                                  | 25     |
| Design debt        | Non-optimal decisions                                 | Non-optimal design decisions are adopted.                                                                                                                                                             | 935    |
| Documentation debt | Low-quality documentation                             | The documentation has been updated reflecting the changes in the system, but quality of updated documentation is low.                                                                                 | 342    |
|                    | Outdated documentation                                | A function or class is added, removed, or modified in the system, but the documentation has not been updated to reflect the change.                                                                   | 144    |
| Requirement debt   | Requirements partially implemented                    | Requirements are implemented, but some are not fully implemented.                                                                                                                                     | 67     |
|                    | Non-functional requirements not being fully satisfied | Non-functional requirements (e.g. availability, capacity, concurrency, extensibility), as described by scenarios, are not fully satisfied.                                                            | 29     |
| Test debt          | Expensive tests                                       | Tests are expensive, resulting in slowing down testing activities. Extra refactoring actions are needed to simplify tests.                                                                            | 28     |
|                    | Flaky tests                                           | Tests fail or pass intermittently for the same configuration.                                                                                                                                         | 83     |
|                    | Lack of tests                                         | A function is added, but no tests are added to cover the new function.                                                                                                                                | 158    |
|                    | Low coverage                                          | Only part of the source code is executed during testing.                                                                                                                                              | 69     |


## Getting Started With SATD Detector

### Requirements

- nltk
- fasttext
- numpy
- tensorflow


### Identifying SATD

1. Download the model weight and word embedding files from [LINK](https://zenodo.org/record/7821209).
2. Replace the file path with the real path and run the following command:

```bash
python3 satd_detector.py 
      --weight_file "{PATH}/satd_detector_for_issues.hdf5" 
      --word_embedding_file "{PATH}/fasttext_issue_300.bin" 
```


### Example Output

```
1/1 [==============================] - 0s 117ms/step
Text: to make their code more readable. I would like to see something like this in the API.
Predicted label: SATD

1/1 [==============================] - 0s 8ms/step
Text: cluster service : add a cluster service based on JGroups Raft
Predicted label: non-SATD

1/1 [==============================] - 0s 7ms/step
Text: Would you be able to build an unit test of this sample code so we can take that and add to the tests of camel-cxf and work on a fix.
Predicted label: SATD

1/1 [==============================] - 0s 13ms/step
Text: I'm raising a new Jira for this.
Predicted label: non-SATD

1/1 [==============================] - 0s 9ms/step
Text: We also need to update the mail wiki page with this feature.
Predicted label: SATD

1/1 [==============================] - 0s 8ms/step
Text: Fix pom.xml files to support nexus based release process
Predicted label: non-SATD

1/1 [==============================] - 0s 10ms/step
Text: The component docs are in adoc files with the source code - the wiki is dead so don't update there. Make sure to fix/update in adoc, and if you want you can do wiki too. But wiki only changes will be lost in the future when wiki is discarded completely
Predicted label: SATD
```


## Paper

Latest version available on [arXiv](https://arxiv.org/abs/2202.02180)

Please adequately refer to this paper any time this dataset is being used. If you publish a paper where this dataset
helps your research, we encourage you to cite the following paper in your publication:

```
@article{li2022identifying,
  title={Identifying self-admitted technical debt in issue tracking systems using machine learning},
  author={Li, Yikun and Soliman, Mohamed and Avgeriou, Paris},
  journal={Empirical Software Engineering},
  volume={27},
  number={6},
  pages={131},
  year={2022},
  publisher={Springer}
}
```


## Contact

- Please use the following email addresses if you have questions:
    - :email: <yikun.li@rug.nl>
