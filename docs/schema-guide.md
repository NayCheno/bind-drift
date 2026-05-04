# BindDrift Schema Guide

## Reader And Goal

This guide is for maintainers extending extractors, detectors, or evaluation scripts. After reading it, they should know which facts each stage writes and how those facts connect.

## Core Tables

`versions` records Linux revisions and toolchain metadata. `commits` records commit messages, changed files, and coarse Rust/C API labels.

`binding_functions`, `binding_structs`, `binding_consts`, and `layout_facts` store bindgen output facts from the kernel object tree.

`rust_binding_uses`, `rust_safe_apis`, and `rust_safety_comments` store Rust wrapper usage facts from Rust-for-Linux abstraction code.

`c_functions`, `c_structs`, `c_macros`, and `c_behavior_indicators` store C-side signatures, declarations, constants, and contract indicators.

`graph_nodes` and `graph_edges` store the C-to-Rust dependency graph. Edges use names such as `GENERATED_FROM`, `CALLS_BINDING`, `EXPOSES_SAFE_API`, and `HAS_SAFETY_COMMENT`.

## Warning Records

Warnings are JSON objects with these stable fields:

- `warning_id`
- `type`
- `risk`
- `score`
- `c_side`
- `rust_side`
- `explanation`
- `suggested_action`
- `confidence`

Tier 2 warnings include `indicator_based: true` and `not_a_bug_claim: true` to preserve the paper claim boundary.

## Versioning Rule

Every extracted fact includes a `version_id`. Detectors compare facts with matching symbols across two version ids. Single-version pilot mode can still generate graph and indicator facts, but objective drift detection requires at least two versions.
