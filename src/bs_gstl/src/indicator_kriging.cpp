/*

    Copyright 2009 HPGL Team

    This file is part of HPGL (High Perfomance Geostatistics Library).

    HPGL is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2 of the License.

    HPGL is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with HPGL. If not, see http://www.gnu.org/licenses/.

*/


#include "stdafx.h"
#include "typedefs.h"
#include "property_array.h"
#include "sugarbox_grid.h"
#include "ik_params.h"
#include "indicator_kriging.h"
#include "pretty_printer.h"
#include "mean_provider.h"
#include "sugarbox_indexed_neighbour_lookup.h"

namespace hpgl
{
void indicator_kriging(
	const indicator_property_array_t & input,
	const sugarbox_grid_t & grid,  //TODO: ������� ��� grid_size_t �������� ������� �����, � ��� ������� �������� ��������� ������� ����������
	const ik_params_t & params,
	indicator_property_array_t & output)
{
	std::vector<boost::shared_ptr<single_mean_t> > single_means;
	create_means(params.m_marginal_probs, single_means);
	do_indicator_kriging(input, grid, params, single_means, output);
}

}
