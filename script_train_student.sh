#!/bin/bash

python train_student.py \
	--teachers_dir XXX \
	--train_dir    checkpoints \
	--data_dir     RAW_DATA \
	--dataset      mnist \
	--nb_labels           10 \
	--lap_scale           10 \
        --stdnt_share         1000 \
	--max_steps           150 \
	--teachers_max_steps  150 \
	--nb_teachers         3 

