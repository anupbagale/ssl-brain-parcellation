# Writes splits/folds.json with file names only (Drive paths removed).
# Run in Colab after mounting Drive, then copy the output into splits/folds.json.
import json, os

SRC = '/content/drive/MyDrive/brain_seg_supervised/cv_results/folds.json'
DST = '/content/splits_folds.json'

folds = json.load(open(SRC))
clean = []
for f in folds:
    clean.append({
        'fold':  f['fold'],
        'train': [os.path.basename(p) for p in f['train']],
        'val':   [os.path.basename(p) for p in f['val']],
        'test':  [os.path.basename(p) for p in f['test']],
    })
json.dump(clean, open(DST, 'w'), indent=2)

n_test = sum(len(f['test']) for f in clean)
print(f"saved {DST}: {len(clean)} folds, {n_test} test subjects")
for f in clean:
    print(f"  fold {f['fold']}: train={len(f['train'])} val={len(f['val'])} test={len(f['test'])}")
assert n_test == 148
