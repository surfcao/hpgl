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
from python_property import *
from matplotlib import *
from numpy import *
from scipy import *
from pylab import *

def mean_calc_hist(x,y,z,n,prop):
    print "Creating Grid... "
    grid = SugarboxGrid(x,y,z)
    print "Done.\n"
    print "Loading property... "
    prop = load_cont_property("NEW_TEST_PROP.INC",-99)
    print "Done.\n"
    ntg1 = empty( (n) )
    for c in xrange(n):
        sgs_params = {
                        "sill":0.4,
                        "radiuses":(20,20,20),
                        "max_neighbours":12,
                        "covariance_types":covariance.exponential,
                        "ranges":(10,10,10)
                    }
        print "Done.\n"
        sgs_result_prop = sgs_simulation(prop, grid,
                                         radiuses = (20,20,20),
                                         seed=3141347-1000*c+500,
                                         max_neighbours = 12,
                                         covariance_type = covariance.exponential,
                                         ranges = (10,10,10),
                                         sill = 0.4)
        write_property(sgs_result_prop, "RSGS.INC", "SGS_PROP", -99)
        values_result = load_property_python(x,y,z,"RSGS.INC",intype)

        all_r = 0.0
        numb = 0.0
        
        for i in xrange(x):
            for j in xrange (y):
                for k in xrange(z):
                     all_r = all_r + values_result[i,j,k]
                     numb = numb + 1
        ntg1[c]=all_r/numb
        print ntg1[c]
        del(sgs_result_prop)
    hist(ntg1, histtype='bar', orientation='vertical')
    show()
