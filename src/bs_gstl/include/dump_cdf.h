/*
   Copyright 2009 HPGL Team
   This file is part of HPGL (High Perfomance Geostatistics Library).
   HPGL is free software: you can redistribute it and/or modify it under the terms of the BSD License.
   You should have received a copy of the BSD License along with HPGL.

*/


#ifndef __DUMP_CDF_H__39AA1806_E473_45FB_A291_6303E13BFEF0__
#define __DUMP_CDF_H__39AA1806_E473_45FB_A291_6303E13BFEF0__

#include <get_compile_time.h>


namespace hpgl
{



	template <typename T, typename Ostream>
	void dump_cdf(const Non_parametric_cdf<T> & cdf, Ostream & stream)
	{
		typename Non_parametric_cdf<T>::const_z_iterator it, end_it;
		for (it = cdf.z_begin(), end_it = cdf.z_end(); it != end_it; ++it)
		{
			stream << *it << ", " << cdf.prob(*it) << '\n';
		}
		stream.flush();
	}

	template <typename T>
	void dump_cdf_to_file(const Non_parametric_cdf<T> & cdf, const std::string & file_name)
	{
		std::string fn = file_name + "_"__DATE__"_" + get_compile_time();
		std::ofstream out(
				fn.c_str(),
				std::ios_base::trunc);
		dump_cdf<T, std::ofstream>(cdf, out);
		out.close();
	}
}

#endif //__DUMP_CDF_H__39AA1806_E473_45FB_A291_6303E13BFEF0__
