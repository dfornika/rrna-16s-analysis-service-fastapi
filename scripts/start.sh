#!/usr/bin/env bash

export RRNA_16S_DATABASE_URI="sqlite:///app.db"

uvicorn rrna_16s_analysis.main:app --reload
