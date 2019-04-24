#!/bin/env bash

#getSNsys

sh getstats_JLA.sh
sh plot_JLA.sh

sh getstats_Pantheon.sh
sh plot_Pantheon.sh

top
