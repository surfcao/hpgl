/*

    Copyright 2009 HPGL Team

    This file is part of HPGL (High Perfomance Geostatistics Library).

    HPGL is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2 of the License.

    HPGL is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with HPGL. If not, see http://www.gnu.org/licenses/.

*/


#include "stdafx.h"
#include "typedefs.h"

namespace hpgl
{
	void extract_indicator_values(
		boost::python::list values,
		int expected_count,
		std::vector<indicator_value_t> & result)
	{
		int iv_length = boost::python::len(values);
		int i_count = expected_count;
		if (iv_length >= i_count)
		{	
			if (iv_length > i_count)
				std::cout << "Warning: Property has " << i_count << " indicators, but " << iv_length << " values given. Extra values are ignored." << std::endl;
			for (int i = 0; i < i_count; ++i)
			{
				result.push_back((int)boost::python::extract<int>(values[i]));
			}
		}
		else
		{
			std::cout << "Warning: Property has " << i_count << " indicators, but " << iv_length << " values given. Values are ignored. Using [0, 1, 2, ...] instead" << std::endl;
			for (int i = 0; i < i_count; ++i)
			{
				result.push_back(i);
			}
		}
	}
}