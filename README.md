# ssl-brain-parcellation

Masked-volume self-supervised pretraining for whole-brain MRI parcellation with few labeled scans.

A 3D residual U-Net (MONAI) is pretrained by reconstructing masked regions of T1-weighted volumes, then fine-tuned to segment 27 FreeSurfer `aseg` structures. Pretraining uses only the training images of each cross-validation fold. The pretrained and randomly initialized models are compared at 10, 25, 50 and 104 labeled scans with 5-fold cross-validation on 148 OASIS-3 subjects. SynthSeg and FastSurfer, used as released, are scored on the same test folds for reference.

## Results

Mean test Dice over 27 structures (background excluded), mean ± SD over 5 folds.

| Labeled scans | Random init | SSL pretrained | Difference | Corrected p |
|---:|:---:|:---:|:---:|:---:|
| 10  | 0.5914 ± 0.0325 | 0.6393 ± 0.0551 | +0.0480 | 0.039 |
| 25  | 0.7043 ± 0.0266 | 0.7652 ± 0.0152 | +0.0610 | 0.005 |
| 50  | 0.7804 ± 0.0086 | 0.7904 ± 0.0232 | +0.0100 | 0.539 |
| 104 | 0.7997 ± 0.0194 | 0.8140 ± 0.0162 | +0.0143 | 0.080 |

p values use the corrected resampled t-test (Nadeau and Bengio, 2003).

### SynthSeg and FastSurfer

Neither tool was trained on these scans. SynthSeg does not segment the choroid plexus, so it is compared over the other 25 structures. FastSurfer's cortical parcels are merged into left and right cortex, which gives all 27 structures. Mean ± SD over the same 5 test folds.

| Method | Labeled scans | Dice, 25 structures | Dice, 27 structures |
|---|---:|:---:|:---:|
| SynthSeg 2.0 | – | 0.8457 ± 0.0071 | – |
| FastSurfer | – | – | 0.8203 ± 0.0074 |
| Random init | 10  | 0.6150 ± 0.0368 | 0.5914 ± 0.0325 |
| SSL pretrained | 10  | 0.6645 ± 0.0540 | 0.6393 ± 0.0551 |
| Random init | 25  | 0.7264 ± 0.0287 | 0.7043 ± 0.0266 |
| SSL pretrained | 25  | 0.7855 ± 0.0161 | 0.7652 ± 0.0152 |
| Random init | 50  | 0.8010 ± 0.0095 | 0.7804 ± 0.0086 |
| SSL pretrained | 50  | 0.8097 ± 0.0238 | 0.7904 ± 0.0232 |
| Random init | 104 | 0.8167 ± 0.0188 | 0.7997 ± 0.0194 |
| SSL pretrained | 104 | 0.8301 ± 0.0152 | 0.8140 ± 0.0162 |

Both tools score higher than every trained model. With 104 labeled scans the pretrained model is within 0.016 Dice of SynthSeg (corrected p = 0.117) and 0.006 of FastSurfer (p = 0.478).

### Boundary distances and volume agreement

Computed after keeping the largest connected component of each predicted structure. HD95 is the 95th-percentile Hausdorff distance and ASSD the average symmetric surface distance (mean ± SD over 5 folds). Volume r is the median over structures of the Pearson correlation with the FreeSurfer volumes; volume difference is the mean absolute percentage difference. SynthSeg covers 25 structures, the others 27.

| Method | Labeled scans | Dice | HD95 (mm) | ASSD (mm) | Volume r | Volume difference (%) |
|---|---:|:---:|:---:|:---:|:---:|:---:|
| Random init | 25  | 0.7224 | 8.91 ± 2.72 | 3.669 ± 1.936 | 0.56 | 23.1 |
| SSL pretrained | 25  | 0.7810 | 4.94 ± 0.19 | 1.344 ± 0.052 | 0.73 | 16.0 |
| Random init | 104 | 0.8077 | 4.67 ± 0.68 | 1.237 ± 0.311 | 0.76 | 14.1 |
| SSL pretrained | 104 | 0.8231 | 3.84 ± 0.43 | 0.953 ± 0.136 | 0.77 | 11.7 |
| SynthSeg 2.0 | – | 0.8459 | 2.11 ± 0.05 | 0.658 ± 0.025 | 0.86 | 11.5 |
| FastSurfer | – | 0.8194 | 3.89 ± 0.08 | 0.942 ± 0.030 | 0.91 | 14.2 |

Pretraining lowered HD95 and ASSD in all five folds at both budgets. After the correction for dependent folds, only the HD95 reduction at 104 labeled scans is significant (p = 0.044).

The summary tables are in `results/`.

## Notebooks

| Notebook | Description | |
|---|---|---|
| `01_training_and_label_efficiency.ipynb` | 5-fold CV baseline, SSL pretraining, label-efficiency runs, statistics, per-structure results | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/ssl-brain-parcellation/blob/main/notebooks/01_training_and_label_efficiency.ipynb) |
| `02_clinical_analysis.ipynb` | Per-subject Dice vs CDR, MMSE, age, sex and scanner, and scanner vs disease | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/ssl-brain-parcellation/blob/main/notebooks/02_clinical_analysis.ipynb) |
| `04_synthseg_reference.ipynb` | SynthSeg 2.0 (FreeSurfer 7.4.1) on all scans, Dice over 25 structures against the trained models | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/ssl-brain-parcellation/blob/main/notebooks/04_synthseg_reference.ipynb) |
| `05_baselines_volume_boundary.ipynb` | FastSurfer on all scans, volume agreement, HD95 and ASSD for the trained models and both tools, scanner check | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anupbagale/ssl-brain-parcellation/blob/main/notebooks/05_baselines_volume_boundary.ipynb) |

Run 01 first. Notebook 04 needs the result files of 01, and notebook 05 needs the checkpoints of 01 and the SynthSeg outputs of 04.

## Contents

```
notebooks/   the notebooks above
results/     summary tables (no per-subject values)
scripts/     export_clean_folds.py: writes splits/folds.json (file names only)
splits/      folds.json: train / val / test files for each fold
```

## Setup

The experiments were run on Google Colab. Notebook 01 used an A100 GPU, notebook 05 a T4 GPU, and notebooks 02 and 04 run on CPU.

```
pip install -r requirements.txt
```

Versions used: PyTorch 2.11, MONAI 1.7 (`monai-weekly`).

- Notebook 04 downloads FreeSurfer 7.4.1 (about 5 GB) and runs `mri_synthseg` with `--cpu --crop 192`, one scan per call.
- Notebook 05 clones FastSurfer (stable branch; commit a314cd4 was used) and runs the segmentation module only (`--seg_only --no_cc`).

## Data

This repository does not contain any OASIS-3 images, labels or clinical data. They cannot be redistributed under the OASIS data use agreement.

1. Request access to OASIS-3 at https://www.oasis-brains.org.
2. Download the T1-weighted volumes and their FreeSurfer `aseg` label maps (256³, 1 mm). One session per subject was used. The file names are listed in `splits/folds.json`.
3. Put images and labels in two folders with the same sorted order and set `IMAGE_DIR` and `LABEL_DIR` in notebook 01.
4. Set `LUT_PATH` to `FreeSurferColorLUT.txt` from FreeSurfer (used only for structure names).
5. For notebook 02, make a metadata CSV from the OASIS-3 clinical and MR session tables with the columns listed at the top of the notebook.
6. Notebooks 04 and 05 use the same `IMAGE_DIR`, `LABEL_DIR` and `ROOT_DIR` as notebook 01. Their segmentations and per-subject metrics are written to `ROOT_DIR/synthseg` and `ROOT_DIR/extra_analysis` and are not part of this repository.

## Labels

28 classes: background and 27 `aseg` structures. These are left and right cerebral white matter, cerebral cortex, lateral ventricle, cerebellar white matter, cerebellar cortex, thalamus, caudate, putamen, pallidum, hippocampus, ventral DC and choroid plexus, plus 3rd ventricle, 4th ventricle and brainstem. All other `aseg` labels are set to background.

## Reproducibility

- Seed 42 is used for the fold split, subset selection, patch sampling and initialization.
- `splits/folds.json` gives the exact split, so each run can be repeated on the same subjects.
- SSL pretraining is run separately in each fold on that fold's training subjects. Validation and test subjects are not used.
- Notebooks 04 and 05 rebuild the same test folds from seed 42, so the tools are compared with each model on identical subjects.

## Acknowledgments

Data were provided by OASIS-3: Longitudinal Multimodal Neuroimaging: Principal Investigators: T. Benzinger, D. Marcus, J. Morris; NIH P30 AG066444, P50 AG00561, P30 NS09857781, P01 AG026276, P01 AG003991, R01 AG043434, UL1 TR000448, R01 EB009352. The data are available through NITRC (https://www.nitrc.org).

SynthSeg (Billot et al., 2023) and FastSurfer (Henschel et al., 2020) were used as released by their authors.

## License

MIT (see `LICENSE`). The license applies to the code only.
