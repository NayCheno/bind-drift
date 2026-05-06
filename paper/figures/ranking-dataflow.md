# Figure: Oracle-Blind Ranking Data Flow

```mermaid
flowchart LR
  subgraph D["Detection-time features"]
    C["C-side drift facts"]
    B["Generated binding diffs"]
    R["Rust exposure evidence"]
    E["Evidence-chain features"]
  end

  subgraph P["Primary oracle-blind ranking"]
    S["BindDrift-oracle-blind score"]
    K["Top-K review targets"]
  end

  subgraph A["Auxiliary validation oracles"]
    BO["Build-breakage oracle"]
    WO["Wrapper-fix oracle"]
    L["Labels and auxiliary validation"]
  end

  subgraph V["Evaluation and validation"]
    M["Metrics, labels, and audit gates"]
  end

  C --> S
  B --> S
  R --> S
  E --> S
  S --> K
  BO --> L
  WO --> L
  K --> M
  L --> M
```

The primary ranker is `BindDrift-oracle-blind`. Its score uses only
detection-time features. The build-breakage and wrapper-fix oracles feed labels
and auxiliary validation; they do not feed the primary score or Top-K selection.
