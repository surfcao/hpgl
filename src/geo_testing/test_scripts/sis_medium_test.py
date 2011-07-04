#
#
#   Copyright 2009 HPGL Team
#
#   This file is part of HPGL (High Perfomance Geostatistics Library).
#
#   HPGL is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2 of the License.
#
#   HPGL is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License along with HPGL. If not, see http://www.gnu.org/licenses/.
#
from geo import *
from sys import *
import os

if not os.path.exists("results/"):
	os.mkdir("results/")
if not os.path.exists("results/medium/"):
	os.mkdir("results/medium/")

grid = SugarboxGrid(166, 141, 20)

ik_prop = load_ind_property("test_data/BIG_SOFT_DATA_160_141_20.INC", -99, [0,1])
print 'Property data loaded.'

ik_data =  [	{
			"cov_type": 1, 
		        "ranges": (10, 10, 10),
			"sill": 1,
			"radiuses": (20, 20, 20),
			"max_neighbours": 12,
			"marginal_prob": 0.8,
			"value": 0
		},
		{
			"cov_type": 1, 
			"ranges": (10, 10, 10),
			"sill": 1,
			"radiuses": (20, 20, 20),
			"max_neighbours": 12,
			"marginal_prob": 0.2,
			"value": 1
		}]

sis_result = sis_simulation(ik_prop, grid, ik_data, seed=3241347)
write_property(sis_result, "results/medium/sis_medium.inc", "SIS_MEDIUM", -99)
