---
title: Coverage
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/coverage

flamapy_sat: true
flamapy_bdd: false
flamapy_fm: false
flamapy_z3: false
flamapy_diagnosis: false
flamapy_sharpsat: false
flamapy_sdd: false
flamapy_dnnf: false
cmd: false
facade: true
python: true
rest: true
---

# Coverage

**Description**:
Measures the t-wise coverage of a configuration suite: the fraction of all satisfiable combinations of ``t`` feature selections that are covered by at least one of the given configurations (1.0 = full coverage).

**Application**:
Assesses how well a test suite of configurations exercises the feature interactions of a product line (e.g. before running expensive tests on each product).

**Example**:
A suite of 10 random configurations may reach 0.89 pairwise coverage, i.e. it covers 89% of the valid pairs of feature selections.

---
## Code Examples

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# Measure the pairwise (t=2) coverage of a configuration suite
sample = fm.sampling(size=10)
result = fm.coverage(sample, t=2)
print(result)
```

### Python flamapy framework **ADVANCED** usage
```python
from flamapy.core.discover import DiscoverMetamodels
# Initialize the discover metamodel
dm = DiscoverMetamodels()
# Get the fm metamodel representation using the transformation
# required to get to the fm metamodel
feature_model = dm.use_transformation_t2m("path/to/feature/model", 'fm')
# Manually call a M2M transformation to PySAT
sat_model = dm.use_transformation_m2m(feature_model, "pysat")
# Build the configuration suite to analyse, e.g. with a random sample
sampling = dm.get_operation(sat_model, 'PySATSampling')
sampling.set_sample_size(10)
sample = sampling.execute(sat_model).get_result()
# Get the operation
operation = dm.get_operation(sat_model, 'PySATCoverage')
# Set the configurations to measure and the interaction strength
operation.set_configurations(sample)
operation.set_t(2)
# Execute the operation
operation.execute(sat_model)
# Get and print the result
result = operation.get_result()
print(result)
```

---

<!-- BEGIN GENERATED: operation reference (bin/generate_operation_docs.py) -->

**Facade signature**: `coverage(self, configurations: Any, t: int = 2)`

**Inputs**:

| name | type | required | default |
|------|------|----------|---------|
| `configurations` | Any | yes | — |
| `t` | int | no | 2 |

**Default backend**: sat

**Implemented by**:

| plugin | exact | scale limit |
|--------|-------|-------------|
| pysat_metamodel | yes | — |

<!-- END GENERATED -->
