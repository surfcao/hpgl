/*

    Copyright 2009 HPGL Team

    This file is part of HPGL (High Perfomance Geostatistics Library).

    HPGL is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2 of the License.

    HPGL is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with HPGL. If not, see http://www.gnu.org/licenses/.

*/


#ifndef __INDICATOR_PARAM_H__C3056059_834A_4CB4_8A17_323EF277959D__
#define __INDICATOR_PARAM_H__C3056059_834A_4CB4_8A17_323EF277959D__

#include <covariance_param.h>
#include <neighbourhood_param.h>

namespace hpgl
{
	class indicator_param_t : private covariance_param_t, private neighbourhood_param_t
	{
	public:
		using covariance_param_t::m_covariance_type;
		using covariance_param_t::m_ranges;
		using covariance_param_t::m_angles;
		using covariance_param_t::m_sill;
		using covariance_param_t::m_nugget;

		using neighbourhood_param_t::m_radiuses;
		using neighbourhood_param_t::m_max_neighbours;

		using covariance_param_t::set_ranges;
		using covariance_param_t::set_angles;
		using neighbourhood_param_t::set_radiuses;

		double m_marginal_prob;
	private:
		unsigned short m_value;
	};
}

#endif //__INDICATOR_PARAM_H__C3056059_834A_4CB4_8A17_323EF277959D__