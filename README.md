# ssl-brain-parcellation

Masked-volume self-supervised pretraining for whole-brain MRI parcellation with few labeled scans.

A 3D residual U-Net (MONAI) is pretrained by reconstructing masked regions of T1-weighted volumes, then fine-tuned to segment 27 FreeSurfer `aseg` structures. Pretraining uses only the training images of each cross-validation fold. The pretrained and randomly initialized models are compared at 10, 25, 50 and 104 labeled scans with 5-fold cross-validation on 148 OASIS-3 subjects.

## Results

Mean test Dice over 27 structures (background excluded), mean ± SD over 5 folds.

| Labeled scans | Random init | SSL pretrained | Difference | Corrected p |
|---:|:---:|:---:|:---:|:---:|
| 10  | 0.5914 ± 0.0325 | 0.6393 ± 0.0551 | +0.0480 | 0.039 |
| 25  | 0.7043 ± 0.0266 | 0.7652 ± 0.0152 | +0.0610 | 0.005 |
| 50  | 0.7804 ± 0.0086 | 0.7904 ± 0.0232 | +0.0100 | 0.539 |
| 104 | 0.7997 ± 0.0194 | 0.8140 ± 0.0162 | +0.0143 | 0.080 |

p values use the corrected resampled t-test (Nadeau and Bengio, 2003).

## Notebooks

| Notebook | Description | |
|---|---|---|
| `01_training_and_label_efficiency.ipynb` | 5-fold CV baseline, SSL pretraining, label-efficiency runs, statistics, per-structure results | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/ssl-brain-parcellation/blob/main/notebooks/01_training_and_label_efficiency.ipynb) |
| `02_clinical_analysis.ipynb` | Per-subject Dice vs CDR, MMSE, age, sex and scanner, and scanner vs disease | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/ssl-brain-parcellation/blob/main/notebooks/02_clinical_analysis.ipynb) |

## Contents

```
notebooks/   the two notebooks above
scripts/     export_clean_folds.py: writes splits/folds.json (file names only)
splits/      folds.json: train / val / test files for each fold
```

## Setup

The experiments were run on Google Colab (A100 GPU).

```
pip install -r requirements.txt
```

Versions used: PyTorch 2.11, MONAI 1.7 (`monai-weekly`). Notebook 02 runs on CPU.

## Data

This repository does not contain any OASIS-3 images, labels or clinical data. They cannot be redistributed under the OASIS data use agreement.

1. Request access to OASIS-3 at https://www.oasis-brains.org.
2. Download the T1-weighted volumes and their FreeSurfer `aseg` label maps (256³, 1 mm). One session per subject was used. The file names are listed in `splits/folds.json`.
3. Put images and labels in two folders with the same sorted order and set `IMAGE_DIR` and `LABEL_DIR` in notebook 01.
4. Set `LUT_PATH` to `FreeSurferColorLUT.txt` from FreeSurfer (used only for structure names).
5. For notebook 02, make a metadata CSV from the OASIS-3 clinical and MR session tables with the columns listed at the top of the notebook.

## Labels

28 classes: background and 27 `aseg` structures. These are left and right cerebral white matter, cerebral cortex, lateral ventricle, cerebellar white matter, cerebellar cortex, thalamus, caudate, putamen, pallidum, hippocampus, ventral DC and choroid plexus, plus 3rd ventricle, 4th ventricle and brainstem. All other `aseg` labels are set to background.

## Reproducibility

- Seed 42 is used for the fold split, subset selection, patch sampling and initialization.
- `splits/folds.json` gives the exact split, so each run can be repeated on the same subjects.
- SSL pretraining is run separately in each fold on that fold's training subjects. Validation and test subjects are not used.

## Acknowledgments

Data were provided by OASIS-3: Longitudinal Multimodal Neuroimaging: Principal Investigators: T. Benzinger, D. Marcus, J. Morris; NIH P30 AG066444, P50 AG00561, P30 NS09857781, P01 AG026276, P01 AG003991, R01 AG043434, UL1 TR000448, R01 EB009352.

## License

MIT (see `LICENSE`). The license applies to the code only.
