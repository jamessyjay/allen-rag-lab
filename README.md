allen-rag-lab/
  docker-compose.yml        # qdrant, opensearch, minio (если надо), ui
  .env.example
  data/                     # кэш NWB/SWC
  notebooks/                # демо-ноуты
  ingest/
    fetch_cells.py          # скачать NWB/SWC + метаданные
    build_metadata.py       # нормализация мета → parquet/jsonl
    docs_ingest.py          # доки AllenSDK/ipfx/whitepapers → векторка
  analysis/
    ephys_features.py       # ipfx: spiking/adaptation/τm/Rin/AP width …
    morpho_features.py      # neurom: длины/ветвления/ширина апикала …
    classify_celltype.py    # простая модель (XGB/LogReg) по фичам
  rag/
    retrievers/
      hybrid.py             # vector + bm25 + RRF + rerank
      graph_rag.py          # (позже) онтология cell types → граф
    prompts/
      system.md
      answer_with_citations.md
    pipeline.py             # сборка: вопрос → ретрив → ответ+цитаты
  reports/
    make_report.py          # HTML/PDF с графиками и цитатами
  tests/
    test_ingest.py
    test_ephys_pipeline.py
    test_rag_faithfulness.py
  README.md