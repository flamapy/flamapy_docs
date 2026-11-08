---
title: Sample reduction
layout: default
parent: Operations
grand_parent: Flamapy as framework
permalink: /framework/operations/sample_reduction

flamapy_sat: true
flamapy_bdd: false
flamapy_fm: false
flamapy_z3: false
flamapy_diagnosis: false
flamapy_sharpsat: false
flamapy_sdd: false
flamapy_dnnf: false
cmd: true
facade: true
python: true
rest: true
---

# Sample reduction

**Description**:
Reduces a configuration suite to a (greedily) minimal subset that preserves exactly the t-wise coverage the full suite already achieves.

**Application**:
Shrinks an existing test suite of configurations without losing any of the `t`-wise feature interactions it already covers, reducing testing cost.

**Example**:
A suite of 20 random configurations can often be reduced to a handful that keeps exactly the same pairwise coverage.

---
## Code Examples

### Python easy to use facade usage
```python
from flamapy.interfaces.python.flamapy_feature_model import FLAMAFeatureModel
# Load the feature model
fm = FLAMAFeatureModel("path/to/feature/model")
# Reduce a configuration suite while keeping its pairwise (t=2) coverage
sample = fm.sampling(size=20)
result = fm.sample_reduction(sample, t=2)
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
sampling.set_sample_size(20)
sample = sampling.execute(sat_model).get_result()
# Get the operation
operation = dm.get_operation(sat_model, 'PySATSampleReduction')
# Set the configurations to reduce and the interaction strength
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

**Facade signature**: `sample_reduction(self, configurations: Any, t: int = 2)`

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
