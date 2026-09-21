# Farmer Knowledge Assistant

An evidence-grounded agricultural knowledge assistant built with RAG,
LangChain, and eventually LangGraph.

## Current Goal

Build a retrieval-augmented system that can answer agricultural
questions using trusted agricultural knowledge sources.

## Architecture

Current:

PDF
↓
Document Loader
↓
Document Objects
↓
Text Chunking
↓
Chunk Inspection

Planned:

Query Analysis
↓
Hybrid Retrieval
├── Vector Search
└── BM25 Search
↓
Reranking
↓
LangGraph Agent
├── Retrieve
├── Verify
└── Reason
↓
Grounded Answer
├── Citations
└── Confidence

## Current Progress

### Phase 1 — Document Ingestion

- [x] Python virtual environment
- [x] LangChain setup
- [x] PDF loading
- [x] Document inspection
- [x] Initial text splitting
- [x] Metadata inspection
- [x] Identified PDF extraction/encoding issues

### Next

- [ ] Document preprocessing
- [ ] Better chunking strategy
- [ ] Chunk quality evaluation
- [ ] Embeddings
- [ ] Vector database
- [ ] Basic RAG pipeline

## Knowledge Source

Initial source:

ICAR Kharif Agro-Advisories for Farmers 2025

The source PDF is kept locally and is not committed to this repository.

## Project Status

Early development / learning project.