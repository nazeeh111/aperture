# Optional GitHub source snapshots

The helper is separate from the Research core and is never required for ordinary browsing.

```sh
python3 research/scripts/snapshot_github.py \
  --repo OWNER/REPOSITORY \
  --commit FULL_40_CHARACTER_COMMIT_SHA \
  --path path/to/file.py \
  --out /absolute/path/to/new-snapshot
```

Repeat `--path` for additional selected files. The destination must be new, and its parent must exist. By default, each file is limited to 4 MiB and each request to 25 seconds. `--max-bytes` and `--timeout` can change those limits; timeout must remain in `(0, 300]` seconds.

The manifest records repository, full revision, requested paths, source URLs, byte counts, hashes and failures. Downloaded content is never executed. Redirects are refused. The first failure stops later requests without retries. Earlier successful files remain alongside the partial-failure manifest. Existing destinations, including symlinks, are refused.

| Exit | Meaning |
| --- | --- |
| `0` | All selected files saved. |
| `1` | Failed, partial or refused snapshot. Inspect the manifest when available. |
| `2` | Invalid CLI arguments. |
| `130` | Interrupted; inspect the destination if created. |

A disk failure may prevent the final manifest update. Hashes identify downloaded bytes, not an independently verified Git blob. Source selection, reading, licensing, permitted access and claim verification remain the caller's responsibility.
