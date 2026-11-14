# results

Summary tables only. Per-subject values are not included (OASIS data use agreement).

From notebook 04 (`ROOT_DIR/synthseg`):

| File | Content |
|---|---|
| `synthseg_vs_ours_25structures.csv` | Dice over 25 structures per test fold: SynthSeg and both models at 10, 25, 50 and 104 labeled scans |
| `synthseg_vs_ours_per_structure.csv` | Dice per structure: SynthSeg and both models at 25 and 104 labeled scans |

From notebook 05 (`ROOT_DIR/extra_analysis`):

| File | Content |
|---|---|
| `table_dice_vs_baselines.csv` | Dice of SynthSeg and FastSurfer against each model, with corrected p values |
| `table_volume_summary.csv` | Volume agreement with FreeSurfer, summarized over structures |
| `table_volume_by_structure.csv` | Volume agreement per structure (mean volumes, Pearson r, percentage difference) |
| `table_boundary_summary.csv` | HD95 and ASSD after largest-component clean-up, mean ± SD over folds |
| `table_boundary_by_structure.csv` | HD95, ASSD and Dice per structure |
| `table_boundary_ssl_vs_random.csv` | Pretrained against randomly initialized: HD95 and ASSD reduction, corrected p values |
| `table_scanner_check.csv` | Dice by scanner, cognitively normal participants only |

The `metrics_*.csv` and `synthseg_dice_per_subject.csv` files hold per-subject values and are not uploaded.
