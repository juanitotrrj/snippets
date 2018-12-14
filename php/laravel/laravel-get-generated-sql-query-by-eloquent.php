<?php
\Illuminate\Support\Facades\DB::connection()->enableQueryLog();
// Perform queries here
SomeModel::all();
\Log::debug(print_r(\Illuminate\Support\Facades\DB::getQueryLog(), true));
// tail -n100 storage/logs/lumen.log
