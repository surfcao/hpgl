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

if not os.path.exists("fixed/"):
	os.mkdir("fixed/")

print "loading double property..."

prop = load_ind_property("test_data/BIG_SOFT_DATA_160_141_20.INC", -99,[0,1])
prop_cont = load_cont_property("test_data/BIG_SOFT_DATA_CON_160_141_20.INC", -99)
prop_cdf = load_cont_property("test_data/BIG_SOFT_DATA_160_141_20.INC", -99)

print "done"

grid = SugarboxGrid(166, 141, 20)


if (not "nook" in argv):
#	while True:
	prop2 = ordinary_kriging(prop_cont, grid,
		radiuses = (20, 20, 20),
		max_neighbours = 12,
		covariance_type = covariance.exponential,
		ranges = (10, 10, 10),
		sill = 1)
	
	write_property(prop2, "fixed/RESULT_OK_BIG.INC", "BIG_OK", -99)
	del(prop2)

if (not "nosk" in argv):

	prop3 = simple_kriging(prop_cont, grid,
		radiuses = (20, 20, 20),
		max_neighbours = 12,
		covariance_type = covariance.exponential,
		ranges = (10, 10, 10),
		sill = 1,
		mean = 1.6)
	
	write_property(prop3, "fixed/RESULT_SK_BIG.INC", "BIG_SK", -99)
	del(prop3)


if (not "nolvm" in argv):
	mean_data = load_mean_data("test_data/mean_0.487_166_141_20.inc")	
	prop_lvm = lvm_kriging(prop_cont, grid, mean_data,
			radiuses = (20, 20, 20),
		max_neighbours = 12,
		covariance_type = covariance.exponential,
		ranges = (10, 10, 10),
		sill = 1)
	
	write_property(prop_lvm, "fixed/lvm.inc", "lvm_medium", -99)
	del(mean_data)
	del(prop_lvm)

if (not "nosgs" in argv):
	
	sgs_params = {
		"radiuses": (20, 20, 20),
		"max_neighbours": 12,
		"covariance_type": covariance.exponential,
		"ranges": (10, 10, 10),
		"sill": 0.4,
		"kriging_type": "sk"}
		
	sgs_params_cdf_not_equal = {
		"radiuses": (20, 20, 20),
		"max_neighbours": 12,
		"covariance_type": covariance.exponential,
		"ranges": (10, 10, 10),
		"sill": 0.4,
		"kriging_type": "sk",
		"cdf_data": prop_cdf}
	mean_data = load_mean_data("test_data/mean_0.487_166_141_20.inc")
	lvm_sgs_params = {
		"radiuses": (20, 20, 20),
		"max_neighbours": 12,
		"covariance_type": covariance.exponential,
		"ranges": (10, 10, 10),
		"sill": 0.4,
		"mean_data": mean_data}
		
	sgs_result1 = sgs_simulation(prop_cont, grid, seed=3439275, **sgs_params)
	write_property(sgs_result1, "fixed/SGS1.INC", "SGS1", -99)

	sgs_result2 = sgs_simulation(prop_cont, grid, seed=24193421, **sgs_params)
	write_property(sgs_result2, "fixed/SGS2.INC", "SGS2", -99)

	sgs_lvm = sgs_simulation(prop_cont, grid, seed=3439275, **lvm_sgs_params)
	write_property(sgs_lvm, "fixed/SGS_LVM.INC", "SGS_LVM", -99)
	
	sgs_cdf_not_equal = sgs_simulation(prop_cont, grid, seed=3439275, **sgs_params_cdf_not_equal)
	write_property(sgs_cdf_not_equal, "fixed/SGS_CDF_NOT_EQUAL.INC", "SGS_CDF_NOT_EQUAL", -99)

	write_property(sgs_result2, "fixed/RESULT_SGS2_BIG.INC", "BIG_SGS2", -99)
	del(sgs_result1)
	del(sgs_result2)
	del(sgs_lvm)

ik_prop = load_ind_property("test_data/BIG_SOFT_DATA_160_141_20.INC", -99,[0,1])

print 'Property data loaded.'


ik_data =  [	{
			"cov_type": 1, 
		    "ranges": (10, 10, 10),
			'sill': 1,
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
		
multi_ik_data = [
	{
		"cov_type": 0,
		"ranges": (4, 4, 4),
		"sill": 0.25,
		"radiuses": (20, 20, 20),
		"max_neighbours": 12,
		"marginal_prob": 0.24,
		"value": 0
	},
	{
		"cov_type": 0,
		"ranges": (6, 6, 6),
		"sill": 0.25,
		"radiuses": (20, 20, 20),
		"max_neighbours": 12,
		"marginal_prob": 0.235,
		"value": 1
	},
	{
		"cov_type": 0,
		"ranges": (2, 2, 2),
		"sill": 0.25,
		"radiuses": (20, 20, 20),
		"max_neighbours": 12,
		"marginal_prob": 0.34,
		"value": 2
	},
	{
		"cov_type": 0,
		"ranges": (10, 10, 10),
		"sill": 0.25,
		"radiuses": (20, 20, 20),
		"max_neighbours": 12,
		"marginal_prob": 0.18,
		"value": 3
	}]		

if (not "noik" in argv):
	ik_result = indicator_kriging(ik_prop, grid, ik_data)
	write_property(ik_result, "fixed/RESULT_IK_BIG_SOFT.INC", "BIG_IK", -99)

if (not "nosis" in argv):
	sis_result = sis_simulation(ik_prop, grid, ik_data, seed=3241347)
	write_property(sis_result, "fixed/RESULT_SIS_BIG_SOFT.INC", "SIS_RESULT_BIG_SOFT", -99)

stdin.readline()
