/*

    Copyright 2009 HPGL Team

    This file is part of HPGL (High Perfomance Geostatistics Library).

    HPGL is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2 of the License.

    HPGL is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with HPGL. If not, see http://www.gnu.org/licenses/.

*/


#ifndef INCLUDED_MEDIAN_IK_H_IN_SOME_BLUE_SKY_PROJECT_SDFLSDKJFLSDFJLSDKFJLSDF
#define INCLUDED_MEDIAN_IK_H_IN_SOME_BLUE_SKY_PROJECT_SDFLSDKJFLSDFJLSDKFJLSDF

#include <typedefs.h>
#include <sugarbox_grid.h>
#include <property_array.h>
#include <search_ellipsoid.h>
#include <ok_params.h>

namespace hpgl
{

	struct median_ik_params : public ok_params_t
	{			
		double m_marginal_probs[2];
	private:
		indicator_value_t m_values[2];	
	};

void median_ik_for_two_indicators(
		const median_ik_params &, 
		const sugarbox_grid_t & grid,
		const property_array_t<indicator_value_t> & input_property,
		property_array_t<indicator_value_t> & output_property
);

}

#endif // INCLUDED_MEDIAN_IK_H_IN_SOME_BLUE_SKY_PROJECT_SDFLSDKJFLSDFJLSDKFJLSDF

