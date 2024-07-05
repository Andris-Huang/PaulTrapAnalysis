#import tensorflow as tf
import numpy as np

from PaulTrapAnalysis.functions import potentials


def Phi(zeta, Mj, order=4, scale=1):
    x, y, z = zeta
    return potentials.generate_potential_single_shot(x, y, z, Mj, order, scale)

def dPhi(zeta, scale=1, Mj=None, order=4):
    Mj = Mj * scale
    x, y, z = zeta
    if order == 4:
        grad = [(-1) * Mj[2] + \
                (6*y) * Mj[3] + (-1.0*x) * Mj[5] + \
                (-3*z) * Mj[6] + (6*x) * Mj[7] + \
                (-90*x*y) * Mj[8] + (30*y*z) * Mj[9] + \
                (3.0*x*y) * Mj[10] + (-3.0*x*z) * Mj[11] + \
                (4.5*x**2 + 1.5*y**2 - 6*z**2) * Mj[12] + (30*x*z) * Mj[13] + \
                (-45*x**2 + 45*y**2) * Mj[14] + (1260*x**2*y - 420*y**3) * Mj[15] + \
                (-630*x*y*z) * Mj[16] + (-45*x**2*y - 15*y**3 + 90*y*z**2) * Mj[17] + \
                (15.0*x*y*z) * Mj[18] + (1.5*x**3 + 1.5*x*y**2 - 6*x*z**2) * Mj[19] + \
                (-10*z**3 + z*(22.5*x**2 + 7.5*y**2)) * Mj[20] + (-30.0*x**3 + 90*x*z**2) * Mj[21] + \
                (z*(-315*x**2 + 315*y**2)) * Mj[22] + (420*x**3 - 1260*x*y**2) * Mj[23], 

                (-1) * Mj[0] + \
                (6*x) * Mj[3] + (-3*z) * Mj[4] + \
                (-1.0*y) * Mj[5] + (-6*y) * Mj[7] + \
                (-45*x**2 + 45*y**2) * Mj[8] + (30*x*z) * Mj[9] + \
                (1.5*x**2 + 4.5*y**2 - 6*z**2) * Mj[10] + (-3.0*y*z) * Mj[11] + \
                (3.0*x*y) * Mj[12] + (-30*y*z) * Mj[13] + \
                (90*x*y) * Mj[14] + (420*x**3 - 1260*x*y**2) * Mj[15] + \
                (z*(-315*x**2 + 315*y**2)) * Mj[16] + (-15*x**3 - 45*x*y**2 + 90*x*z**2) * Mj[17] + \
                (-10*z**3 + z*(7.5*x**2 + 22.5*y**2)) * Mj[18] + (1.5*x**2*y + 1.5*y**3 - 6*y*z**2) * Mj[19] + \
                (15.0*x*y*z) * Mj[20] + (30.0*y**3 - 90*y*z**2) * Mj[21] + \
                (630*x*y*z) * Mj[22] + (-1260*x**2*y + 420*y**3) * Mj[23], 

                (1) * Mj[1] + \
                (-3*y) * Mj[4] + (2*z) * Mj[5] + \
                (-3*x) * Mj[6] + (30*x*y) * Mj[9] + \
                (-12*y*z) * Mj[10] + (-1.5*x**2 - 1.5*y**2 + 3*z**2) * Mj[11] + \
                (-12*x*z) * Mj[12] + (15*x**2 - 15*y**2) * Mj[13] + \
                (-315*x**2*y + 105*y**3) * Mj[16] + (180*x*y*z) * Mj[17] + \
                (7.5*x**2*y + 7.5*y**3 - 30*y*z**2) * Mj[18] + (4*z**3 - 2*z*(3*x**2 + 3*y**2)) * Mj[19] + \
                (7.5*x**3 + 7.5*x*y**2 - 30*x*z**2) * Mj[20] + (2*z*(45*x**2 - 45*y**2)) * Mj[21] + \
                (-105*x**3 + 315*x*y**2) * Mj[22]
            ]
    elif order == 5:
        grad = [(-1) * Mj[2] + \
                (6*y) * Mj[3] + (-1.0*x) * Mj[5] + \
                (-3*z) * Mj[6] + (6*x) * Mj[7] + \
                (-90*x*y) * Mj[8] + (30*y*z) * Mj[9] + \
                (3.0*x*y) * Mj[10] + (-3.0*x*z) * Mj[11] + \
                (4.5*x**2 + 1.5*y**2 - 6*z**2) * Mj[12] + (30*x*z) * Mj[13] + \
                (-45*x**2 + 45*y**2) * Mj[14] + (1260*x**2*y - 420*y**3) * Mj[15] + \
                (-630*x*y*z) * Mj[16] + (-45*x**2*y - 15*y**3 + 90*y*z**2) * Mj[17] + \
                (15.0*x*y*z) * Mj[18] + (1.5*x**3 + 1.5*x*y**2 - 6*x*z**2) * Mj[19] + \
                (-10*z**3 + z*(22.5*x**2 + 7.5*y**2)) * Mj[20] + (-30.0*x**3 + 90*x*z**2) * Mj[21] + \
                (z*(-315*x**2 + 315*y**2)) * Mj[22] + (420*x**3 - 1260*x*y**2) * Mj[23] + \
                (-18900*x**3*y + 18900*x*y**3) * Mj[24] + (z*(11340*x**2*y - 3780*y**3)) * Mj[25] + \
                (630.0*x**3*y + 210*x*y**3 - 2520*x*y*z**2) * Mj[26] + (210*y*z**3 - z*(315*x**2*y + 105*y**3)) * Mj[27] + \
                (-7.5*x**3*y - 7.5*x*y**3 + 45.0*x*y*z**2) * Mj[28] + (-10*x*z**3 + z*(7.5*x**3 + 7.5*x*y**2)) * Mj[29] + \
                (-9.375*x**4 - 11.25*x**2*y**2 - 1.875*y**4 - 15*z**4 + z**2*(67.5*x**2 + 22.5*y**2)) * Mj[30] + (-210.0*x**3*z + 210*x*z**3) * Mj[31] + \
                (262.5*x**4 - 315*x**2*y**2 - 157.5*y**4 - z**2*(1260*x**2 - 1260*y**2)) * Mj[32] + (z*(3780*x**3 - 11340*x*y**2)) * Mj[33] + \
                (-4725*x**4 + 28350*x**2*y**2 - 4725*y**4) * Mj[34], 

                (-1) * Mj[0] + \
                (6*x) * Mj[3] + (-3*z) * Mj[4] + \
                (-1.0*y) * Mj[5] + (-6*y) * Mj[7] + \
                (-45*x**2 + 45*y**2) * Mj[8] + (30*x*z) * Mj[9] + \
                (1.5*x**2 + 4.5*y**2 - 6*z**2) * Mj[10] + (-3.0*y*z) * Mj[11] + \
                (3.0*x*y) * Mj[12] + (-30*y*z) * Mj[13] + \
                (90*x*y) * Mj[14] + (420*x**3 - 1260*x*y**2) * Mj[15] + \
                (z*(-315*x**2 + 315*y**2)) * Mj[16] + (-15*x**3 - 45*x*y**2 + 90*x*z**2) * Mj[17] + \
                (-10*z**3 + z*(7.5*x**2 + 22.5*y**2)) * Mj[18] + (1.5*x**2*y + 1.5*y**3 - 6*y*z**2) * Mj[19] + \
                (15.0*x*y*z) * Mj[20] + (30.0*y**3 - 90*y*z**2) * Mj[21] + \
                (630*x*y*z) * Mj[22] + (-1260*x**2*y + 420*y**3) * Mj[23] + \
                (-4725*x**4 + 28350*x**2*y**2 - 4725*y**4) * Mj[24] + (z*(3780*x**3 - 11340*x*y**2)) * Mj[25] + \
                (157.5*x**4 + 315*x**2*y**2 - 262.5*y**4 - z**2*(1260*x**2 - 1260*y**2)) * Mj[26] + (210*x*z**3 - z*(105*x**3 + 315*x*y**2)) * Mj[27] + \
                (-1.875*x**4 - 11.25*x**2*y**2 - 9.375*y**4 - 15*z**4 + z**2*(22.5*x**2 + 67.5*y**2)) * Mj[28] + (-10*y*z**3 + z*(7.5*x**2*y + 7.5*y**3)) * Mj[29] + \
                (-7.5*x**3*y - 7.5*x*y**3 + 45.0*x*y*z**2) * Mj[30] + (210.0*y**3*z - 210*y*z**3) * Mj[31] + \
                (-210*x**3*y - 630.0*x*y**3 + 2520*x*y*z**2) * Mj[32] + (z*(-11340*x**2*y + 3780*y**3)) * Mj[33] + \
                (18900*x**3*y - 18900*x*y**3) * Mj[34], 

                (1) * Mj[1] + \
                (-3*y) * Mj[4] + (2*z) * Mj[5] + \
                (-3*x) * Mj[6] + (30*x*y) * Mj[9] + \
                (-12*y*z) * Mj[10] + (-1.5*x**2 - 1.5*y**2 + 3*z**2) * Mj[11] + \
                (-12*x*z) * Mj[12] + (15*x**2 - 15*y**2) * Mj[13] + \
                (-315*x**2*y + 105*y**3) * Mj[16] + (180*x*y*z) * Mj[17] + \
                (7.5*x**2*y + 7.5*y**3 - 30*y*z**2) * Mj[18] + (4*z**3 - 2*z*(3*x**2 + 3*y**2)) * Mj[19] + \
                (7.5*x**3 + 7.5*x*y**2 - 30*x*z**2) * Mj[20] + (2*z*(45*x**2 - 45*y**2)) * Mj[21] + \
                (-105*x**3 + 315*x*y**2) * Mj[22] + (3780*x**3*y - 3780*x*y**3) * Mj[25] + \
                (-2*z*(1260*x**2*y - 420*y**3)) * Mj[26] + (-105*x**3*y - 105*x*y**3 + 630*x*y*z**2) * Mj[27] + \
                (-60*y*z**3 + 2*z*(22.5*x**2*y + 22.5*y**3)) * Mj[28] + (1.875*x**4 + 3.75*x**2*y**2 + 1.875*y**4 + 5*z**4 - 3*z**2*(5*x**2 + 5*y**2)) * Mj[29] + \
                (-60*x*z**3 + 2*z*(22.5*x**3 + 22.5*x*y**2)) * Mj[30] + (-52.5*x**4 + 52.5*y**4 + 3*z**2*(105*x**2 - 105*y**2)) * Mj[31] + \
                (-2*z*(420*x**3 - 1260*x*y**2)) * Mj[32] + (945*x**4 - 5670*x**2*y**2 + 945*y**4) * Mj[33]
               ]
    elif order == 6:
        grad = [(-1) * Mj[2] + \
                (6*y) * Mj[3] + (-1.0*x) * Mj[5] + \
                (-3*z) * Mj[6] + (6*x) * Mj[7] + \
                (-90*x*y) * Mj[8] + (30*y*z) * Mj[9] + \
                (3.0*x*y) * Mj[10] + (-3.0*x*z) * Mj[11] + \
                (4.5*x**2 + 1.5*y**2 - 6*z**2) * Mj[12] + (30*x*z) * Mj[13] + \
                (-45*x**2 + 45*y**2) * Mj[14] + (1260*x**2*y - 420*y**3) * Mj[15] + \
                (-630*x*y*z) * Mj[16] + (-45*x**2*y - 15*y**3 + 90*y*z**2) * Mj[17] + \
                (15.0*x*y*z) * Mj[18] + (1.5*x**3 + 1.5*x*y**2 - 6*x*z**2) * Mj[19] + \
                (-10*z**3 + z*(22.5*x**2 + 7.5*y**2)) * Mj[20] + (-30.0*x**3 + 90*x*z**2) * Mj[21] + \
                (z*(-315*x**2 + 315*y**2)) * Mj[22] + (420*x**3 - 1260*x*y**2) * Mj[23] + \
                (-18900*x**3*y + 18900*x*y**3) * Mj[24] + (z*(11340*x**2*y - 3780*y**3)) * Mj[25] + \
                (630.0*x**3*y + 210*x*y**3 - 2520*x*y*z**2) * Mj[26] + (210*y*z**3 - z*(315*x**2*y + 105*y**3)) * Mj[27] + \
                (-7.5*x**3*y - 7.5*x*y**3 + 45.0*x*y*z**2) * Mj[28] + (-10*x*z**3 + z*(7.5*x**3 + 7.5*x*y**2)) * Mj[29] + \
                (-9.375*x**4 - 11.25*x**2*y**2 - 1.875*y**4 - 15*z**4 + z**2*(67.5*x**2 + 22.5*y**2)) * Mj[30] + (-210.0*x**3*z + 210*x*z**3) * Mj[31] + \
                (262.5*x**4 - 315*x**2*y**2 - 157.5*y**4 - z**2*(1260*x**2 - 1260*y**2)) * Mj[32] + (z*(3780*x**3 - 11340*x*y**2)) * Mj[33] + \
                (-4725*x**4 + 28350*x**2*y**2 - 4725*y**4) * Mj[34] + (311850*x**4*y - 623700*x**2*y**3 + 62370*y**5) * Mj[35] + \
                (z*(-207900*x**3*y + 207900*x*y**3)) * Mj[36] + (-9450*x**4*y + 1890*y**5 + z**2*(56700*x**2*y - 18900*y**3)) * Mj[37] + \
                (-7560*x*y*z**3 + z*(5670.0*x**3*y + 1890.0*x*y**3)) * Mj[38] + (131.25*x**4*y + 157.5*x**2*y**3 + 26.25*y**5 + 420*y*z**4 - z**2*(1260*x**2*y + 420*y**3)) * Mj[39] + \
                (105.0*x*y*z**3 - z*(52.5*x**3*y + 52.5*x*y**3)) * Mj[40] + (-1.875*x**5 - 3.75*x**3*y**2 - 1.875*x*y**4 - 15.0*x*z**4 + z**2*(22.5*x**3 + 22.5*x*y**2)) * Mj[41] + \
                (-21*z**5 + z**3*(157.5*x**2 + 52.5*y**2) - z*(65.625*x**4 + 78.75*x**2*y**2 + 13.125*y**4)) * Mj[42] + (78.75*x**5 + 52.5*x**3*y**2 - 840*x**3*z**2 - 26.25*x*y**4 + 420*x*z**4) * Mj[43] + \
                (z**3*(-3780*x**2 + 3780*y**2) + z*(2362.5*x**4 - 2835.0*x**2*y**2 - 1417.5*y**4)) * Mj[44] + (-2835.0*x**5 + 9450.0*x**3*y**2 + 4725.0*x*y**4 + z**2*(18900*x**3 - 56700*x*y**2)) * Mj[45] + \
                (z*(-51975*x**4 + 311850*x**2*y**2 - 51975*y**4)) * Mj[46] + (62370*x**5 - 623700*x**3*y**2 + 311850*x*y**4) * Mj[47], 

                (-1) * Mj[0] + \
                (6*x) * Mj[3] + (-3*z) * Mj[4] + \
                (-1.0*y) * Mj[5] + (-6*y) * Mj[7] + \
                (-45*x**2 + 45*y**2) * Mj[8] + (30*x*z) * Mj[9] + \
                (1.5*x**2 + 4.5*y**2 - 6*z**2) * Mj[10] + (-3.0*y*z) * Mj[11] + \
                (3.0*x*y) * Mj[12] + (-30*y*z) * Mj[13] + \
                (90*x*y) * Mj[14] + (420*x**3 - 1260*x*y**2) * Mj[15] + \
                (z*(-315*x**2 + 315*y**2)) * Mj[16] + (-15*x**3 - 45*x*y**2 + 90*x*z**2) * Mj[17] + \
                (-10*z**3 + z*(7.5*x**2 + 22.5*y**2)) * Mj[18] + (1.5*x**2*y + 1.5*y**3 - 6*y*z**2) * Mj[19] + \
                (15.0*x*y*z) * Mj[20] + (30.0*y**3 - 90*y*z**2) * Mj[21] + \
                (630*x*y*z) * Mj[22] + (-1260*x**2*y + 420*y**3) * Mj[23] + \
                (-4725*x**4 + 28350*x**2*y**2 - 4725*y**4) * Mj[24] + (z*(3780*x**3 - 11340*x*y**2)) * Mj[25] + \
                (157.5*x**4 + 315*x**2*y**2 - 262.5*y**4 - z**2*(1260*x**2 - 1260*y**2)) * Mj[26] + (210*x*z**3 - z*(105*x**3 + 315*x*y**2)) * Mj[27] + \
                (-1.875*x**4 - 11.25*x**2*y**2 - 9.375*y**4 - 15*z**4 + z**2*(22.5*x**2 + 67.5*y**2)) * Mj[28] + (-10*y*z**3 + z*(7.5*x**2*y + 7.5*y**3)) * Mj[29] + \
                (-7.5*x**3*y - 7.5*x*y**3 + 45.0*x*y*z**2) * Mj[30] + (210.0*y**3*z - 210*y*z**3) * Mj[31] + \
                (-210*x**3*y - 630.0*x*y**3 + 2520*x*y*z**2) * Mj[32] + (z*(-11340*x**2*y + 3780*y**3)) * Mj[33] + \
                (18900*x**3*y - 18900*x*y**3) * Mj[34] + (62370*x**5 - 623700*x**3*y**2 + 311850*x*y**4) * Mj[35] + \
                (z*(-51975*x**4 + 311850*x**2*y**2 - 51975*y**4)) * Mj[36] + (-1890*x**5 + 9450*x*y**4 + z**2*(18900*x**3 - 56700*x*y**2)) * Mj[37] + \
                (z**3*(-3780*x**2 + 3780*y**2) + z*(1417.5*x**4 + 2835.0*x**2*y**2 - 2362.5*y**4)) * Mj[38] + (26.25*x**5 + 157.5*x**3*y**2 + 131.25*x*y**4 + 420*x*z**4 - z**2*(420*x**3 + 1260*x*y**2)) * Mj[39] + \
                (-21*z**5 + z**3*(52.5*x**2 + 157.5*y**2) - z*(13.125*x**4 + 78.75*x**2*y**2 + 65.625*y**4)) * Mj[40] + (-1.875*x**4*y - 3.75*x**2*y**3 - 1.875*y**5 - 15.0*y*z**4 + z**2*(22.5*x**2*y + 22.5*y**3)) * Mj[41] + \
                (105.0*x*y*z**3 - z*(52.5*x**3*y + 52.5*x*y**3)) * Mj[42] + (26.25*x**4*y - 52.5*x**2*y**3 - 78.75*y**5 + 840*y**3*z**2 - 420*y*z**4) * Mj[43] + \
                (7560*x*y*z**3 + z*(-1890.0*x**3*y - 5670.0*x*y**3)) * Mj[44] + (4725.0*x**4*y + 9450.0*x**2*y**3 - 2835.0*y**5 + z**2*(-56700*x**2*y + 18900*y**3)) * Mj[45] + \
                (z*(207900*x**3*y - 207900*x*y**3)) * Mj[46] + (-311850*x**4*y + 623700*x**2*y**3 - 62370*y**5) * Mj[47], 

                (1) * Mj[1] + \
                (-3*y) * Mj[4] + (2*z) * Mj[5] + \
                (-3*x) * Mj[6] + (30*x*y) * Mj[9] + \
                (-12*y*z) * Mj[10] + (-1.5*x**2 - 1.5*y**2 + 3*z**2) * Mj[11] + \
                (-12*x*z) * Mj[12] + (15*x**2 - 15*y**2) * Mj[13] + \
                (-315*x**2*y + 105*y**3) * Mj[16] + (180*x*y*z) * Mj[17] + \
                (7.5*x**2*y + 7.5*y**3 - 30*y*z**2) * Mj[18] + (4*z**3 - 2*z*(3*x**2 + 3*y**2)) * Mj[19] + \
                (7.5*x**3 + 7.5*x*y**2 - 30*x*z**2) * Mj[20] + (2*z*(45*x**2 - 45*y**2)) * Mj[21] + \
                (-105*x**3 + 315*x*y**2) * Mj[22] + (3780*x**3*y - 3780*x*y**3) * Mj[25] + \
                (-2*z*(1260*x**2*y - 420*y**3)) * Mj[26] + (-105*x**3*y - 105*x*y**3 + 630*x*y*z**2) * Mj[27] + \
                (-60*y*z**3 + 2*z*(22.5*x**2*y + 22.5*y**3)) * Mj[28] + (1.875*x**4 + 3.75*x**2*y**2 + 1.875*y**4 + 5*z**4 - 3*z**2*(5*x**2 + 5*y**2)) * Mj[29] + \
                (-60*x*z**3 + 2*z*(22.5*x**3 + 22.5*x*y**2)) * Mj[30] + (-52.5*x**4 + 52.5*y**4 + 3*z**2*(105*x**2 - 105*y**2)) * Mj[31] + \
                (-2*z*(420*x**3 - 1260*x*y**2)) * Mj[32] + (945*x**4 - 5670*x**2*y**2 + 945*y**4) * Mj[33] + \
                (-51975*x**4*y + 103950*x**2*y**3 - 10395*y**5) * Mj[36] + (2*z*(18900*x**3*y - 18900*x*y**3)) * Mj[37] + \
                (1417.5*x**4*y + 945.0*x**2*y**3 - 472.5*y**5 + 3*z**2*(-3780*x**2*y + 1260*y**3)) * Mj[38] + (1680*x*y*z**3 - 2*z*(420*x**3*y + 420*x*y**3)) * Mj[39] + \
                (-13.125*x**4*y - 26.25*x**2*y**3 - 13.125*y**5 - 105*y*z**4 + 3*z**2*(52.5*x**2*y + 52.5*y**3)) * Mj[40] + (6*z**5 - 4*z**3*(7.5*x**2 + 7.5*y**2) + 2*z*(5.625*x**4 + 11.25*x**2*y**2 + 5.625*y**4)) * Mj[41] + \
                (-13.125*x**5 - 26.25*x**3*y**2 - 13.125*x*y**4 - 105*x*z**4 + 3*z**2*(52.5*x**3 + 52.5*x*y**2)) * Mj[42] + (4*z**3*(210*x**2 - 210*y**2) - 2*z*(210*x**4 - 210*y**4)) * Mj[43] + \
                (472.5*x**5 - 945.0*x**3*y**2 - 1417.5*x*y**4 + 3*z**2*(-1260*x**3 + 3780*x*y**2)) * Mj[44] + (2*z*(4725*x**4 - 28350*x**2*y**2 + 4725*y**4)) * Mj[45] + \
                (-10395*x**5 + 103950*x**3*y**2 - 51975*x*y**4) * Mj[46]
               ]
    else:
        raise NotImplementedError
    return np.array(grad)


def ddPhi(zeta, Mj, order=4):
    x, y, z = zeta
    if order == 4:
        grad = [(-1.00000000000000) * Mj[5] + \
                (6) * Mj[7] + (-90*y) * Mj[8] + \
                (3.0*y) * Mj[10] + (-3.0*z) * Mj[11] + \
                (9.0*x) * Mj[12] + (30*z) * Mj[13] + \
                (-90*x) * Mj[14] + (2520*x*y) * Mj[15] + \
                (-630*y*z) * Mj[16] + (-90*x*y) * Mj[17] + \
                (15.0*y*z) * Mj[18] + (4.5*x**2 + 1.5*y**2 - 6*z**2) * Mj[19] + \
                (45.0*x*z) * Mj[20] + (-90.0*x**2 + 90*z**2) * Mj[21] + \
                (-630*x*z) * Mj[22] + (1260*x**2 - 1260*y**2) * Mj[23],
                (-1.00000000000000) * Mj[5] + \
                (-6) * Mj[7] + (90*y) * Mj[8] + \
                (9.0*y) * Mj[10] + (-3.0*z) * Mj[11] + \
                (3.0*x) * Mj[12] + (-30*z) * Mj[13] + \
                (90*x) * Mj[14] + (-2520*x*y) * Mj[15] + \
                (630*y*z) * Mj[16] + (-90*x*y) * Mj[17] + \
                (45.0*y*z) * Mj[18] + (1.5*x**2 + 4.5*y**2 - 6*z**2) * Mj[19] + \
                (15.0*x*z) * Mj[20] + (90.0*y**2 - 90*z**2) * Mj[21] + \
                (630*x*z) * Mj[22] + (-1260*x**2 + 1260*y**2) * Mj[23],
                (2) * Mj[5] + \
                (-12*y) * Mj[10] + (6*z) * Mj[11] + \
                (-12*x) * Mj[12] + (180*x*y) * Mj[17] + \
                (-60*y*z) * Mj[18] + (-6*x**2 - 6*y**2 + 12*z**2) * Mj[19] + \
                (-60*x*z) * Mj[20] + (90*x**2 - 90*y**2) * Mj[21]] 
    elif order == 5:
        grad = [(-1.00000000000000) * Mj[5] + \
                (6) * Mj[7] + (-90*y) * Mj[8] + \
                (3.0*y) * Mj[10] + (-3.0*z) * Mj[11] + \
                (9.0*x) * Mj[12] + (30*z) * Mj[13] + \
                (-90*x) * Mj[14] + (2520*x*y) * Mj[15] + \
                (-630*y*z) * Mj[16] + (-90*x*y) * Mj[17] + \
                (15.0*y*z) * Mj[18] + (4.5*x**2 + 1.5*y**2 - 6*z**2) * Mj[19] + \
                (45.0*x*z) * Mj[20] + (-90.0*x**2 + 90*z**2) * Mj[21] + \
                (-630*x*z) * Mj[22] + (1260*x**2 - 1260*y**2) * Mj[23] + \
                (-56700*x**2*y + 18900*y**3) * Mj[24] + (22680*x*y*z) * Mj[25] + \
                (1890.0*x**2*y + 210*y**3 - 2520*y*z**2) * Mj[26] + (-630*x*y*z) * Mj[27] + \
                (-22.5*x**2*y - 7.5*y**3 + 45.0*y*z**2) * Mj[28] + (-10*z**3 + z*(22.5*x**2 + 7.5*y**2)) * Mj[29] + \
                (-37.5*x**3 - 22.5*x*y**2 + 135.0*x*z**2) * Mj[30] + (-630.0*x**2*z + 210*z**3) * Mj[31] + \
                (1050.0*x**3 - 630*x*y**2 - 2520*x*z**2) * Mj[32] + (z*(11340*x**2 - 11340*y**2)) * Mj[33] + \
                (-18900*x**3 + 56700*x*y**2) * Mj[34], 

                (-1.00000000000000) * Mj[5] + \
                (-6) * Mj[7] + (90*y) * Mj[8] + \
                (9.0*y) * Mj[10] + (-3.0*z) * Mj[11] + \
                (3.0*x) * Mj[12] + (-30*z) * Mj[13] + \
                (90*x) * Mj[14] + (-2520*x*y) * Mj[15] + \
                (630*y*z) * Mj[16] + (-90*x*y) * Mj[17] + \
                (45.0*y*z) * Mj[18] + (1.5*x**2 + 4.5*y**2 - 6*z**2) * Mj[19] + \
                (15.0*x*z) * Mj[20] + (90.0*y**2 - 90*z**2) * Mj[21] + \
                (630*x*z) * Mj[22] + (-1260*x**2 + 1260*y**2) * Mj[23] + \
                (56700*x**2*y - 18900*y**3) * Mj[24] + (-22680*x*y*z) * Mj[25] + \
                (630*x**2*y - 1050.0*y**3 + 2520*y*z**2) * Mj[26] + (-630*x*y*z) * Mj[27] + \
                (-22.5*x**2*y - 37.5*y**3 + 135.0*y*z**2) * Mj[28] + (-10*z**3 + z*(7.5*x**2 + 22.5*y**2)) * Mj[29] + \
                (-7.5*x**3 - 22.5*x*y**2 + 45.0*x*z**2) * Mj[30] + (630.0*y**2*z - 210*z**3) * Mj[31] + \
                (-210*x**3 - 1890.0*x*y**2 + 2520*x*z**2) * Mj[32] + (z*(-11340*x**2 + 11340*y**2)) * Mj[33] + \
                (18900*x**3 - 56700*x*y**2) * Mj[34], 

                (2) * Mj[5] + \
                (-12*y) * Mj[10] + (6*z) * Mj[11] + \
                (-12*x) * Mj[12] + (180*x*y) * Mj[17] + \
                (-60*y*z) * Mj[18] + (-6*x**2 - 6*y**2 + 12*z**2) * Mj[19] + \
                (-60*x*z) * Mj[20] + (90*x**2 - 90*y**2) * Mj[21] + \
                (-2520*x**2*y + 840*y**3) * Mj[26] + (1260*x*y*z) * Mj[27] + \
                (45.0*x**2*y + 45.0*y**3 - 180*y*z**2) * Mj[28] + (20*z**3 - 6*z*(5*x**2 + 5*y**2)) * Mj[29] + \
                (45.0*x**3 + 45.0*x*y**2 - 180*x*z**2) * Mj[30] + (6*z*(105*x**2 - 105*y**2)) * Mj[31] + \
                (-840*x**3 + 2520*x*y**2) * Mj[32]
               ]
    elif order == 6:
        grad = [(-1.00000000000000) * Mj[5] + \
                (6) * Mj[7] + (-90*y) * Mj[8] + \
                (3.0*y) * Mj[10] + (-3.0*z) * Mj[11] + \
                (9.0*x) * Mj[12] + (30*z) * Mj[13] + \
                (-90*x) * Mj[14] + (2520*x*y) * Mj[15] + \
                (-630*y*z) * Mj[16] + (-90*x*y) * Mj[17] + \
                (15.0*y*z) * Mj[18] + (4.5*x**2 + 1.5*y**2 - 6*z**2) * Mj[19] + \
                (45.0*x*z) * Mj[20] + (-90.0*x**2 + 90*z**2) * Mj[21] + \
                (-630*x*z) * Mj[22] + (1260*x**2 - 1260*y**2) * Mj[23] + \
                (-56700*x**2*y + 18900*y**3) * Mj[24] + (22680*x*y*z) * Mj[25] + \
                (1890.0*x**2*y + 210*y**3 - 2520*y*z**2) * Mj[26] + (-630*x*y*z) * Mj[27] + \
                (-22.5*x**2*y - 7.5*y**3 + 45.0*y*z**2) * Mj[28] + (-10*z**3 + z*(22.5*x**2 + 7.5*y**2)) * Mj[29] + \
                (-37.5*x**3 - 22.5*x*y**2 + 135.0*x*z**2) * Mj[30] + (-630.0*x**2*z + 210*z**3) * Mj[31] + \
                (1050.0*x**3 - 630*x*y**2 - 2520*x*z**2) * Mj[32] + (z*(11340*x**2 - 11340*y**2)) * Mj[33] + \
                (-18900*x**3 + 56700*x*y**2) * Mj[34] + (1247400*x**3*y - 1247400*x*y**3) * Mj[35] + \
                (z*(-623700*x**2*y + 207900*y**3)) * Mj[36] + (-37800*x**3*y + 113400*x*y*z**2) * Mj[37] + \
                (-7560*y*z**3 + z*(17010.0*x**2*y + 1890.0*y**3)) * Mj[38] + (525.0*x**3*y + 315.0*x*y**3 - 2520*x*y*z**2) * Mj[39] + \
                (105.0*y*z**3 - z*(157.5*x**2*y + 52.5*y**3)) * Mj[40] + (-9.375*x**4 - 11.25*x**2*y**2 - 1.875*y**4 - 15.0*z**4 + z**2*(67.5*x**2 + 22.5*y**2)) * Mj[41] + \
                (315.0*x*z**3 - z*(262.5*x**3 + 157.5*x*y**2)) * Mj[42] + (393.75*x**4 + 157.5*x**2*y**2 - 2520*x**2*z**2 - 26.25*y**4 + 420*z**4) * Mj[43] + \
                (-7560*x*z**3 + z*(9450.0*x**3 - 5670.0*x*y**2)) * Mj[44] + (-14175.0*x**4 + 28350.0*x**2*y**2 + 4725.0*y**4 + z**2*(56700*x**2 - 56700*y**2)) * Mj[45] + \
                (z*(-207900*x**3 + 623700*x*y**2)) * Mj[46] + (311850*x**4 - 1871100*x**2*y**2 + 311850*y**4) * Mj[47], 

                (-1.00000000000000) * Mj[5] + \
                (-6) * Mj[7] + (90*y) * Mj[8] + \
                (9.0*y) * Mj[10] + (-3.0*z) * Mj[11] + \
                (3.0*x) * Mj[12] + (-30*z) * Mj[13] + \
                (90*x) * Mj[14] + (-2520*x*y) * Mj[15] + \
                (630*y*z) * Mj[16] + (-90*x*y) * Mj[17] + \
                (45.0*y*z) * Mj[18] + (1.5*x**2 + 4.5*y**2 - 6*z**2) * Mj[19] + \
                (15.0*x*z) * Mj[20] + (90.0*y**2 - 90*z**2) * Mj[21] + \
                (630*x*z) * Mj[22] + (-1260*x**2 + 1260*y**2) * Mj[23] + \
                (56700*x**2*y - 18900*y**3) * Mj[24] + (-22680*x*y*z) * Mj[25] + \
                (630*x**2*y - 1050.0*y**3 + 2520*y*z**2) * Mj[26] + (-630*x*y*z) * Mj[27] + \
                (-22.5*x**2*y - 37.5*y**3 + 135.0*y*z**2) * Mj[28] + (-10*z**3 + z*(7.5*x**2 + 22.5*y**2)) * Mj[29] + \
                (-7.5*x**3 - 22.5*x*y**2 + 45.0*x*z**2) * Mj[30] + (630.0*y**2*z - 210*z**3) * Mj[31] + \
                (-210*x**3 - 1890.0*x*y**2 + 2520*x*z**2) * Mj[32] + (z*(-11340*x**2 + 11340*y**2)) * Mj[33] + \
                (18900*x**3 - 56700*x*y**2) * Mj[34] + (-1247400*x**3*y + 1247400*x*y**3) * Mj[35] + \
                (z*(623700*x**2*y - 207900*y**3)) * Mj[36] + (37800*x*y**3 - 113400*x*y*z**2) * Mj[37] + \
                (7560*y*z**3 + z*(5670.0*x**2*y - 9450.0*y**3)) * Mj[38] + (315.0*x**3*y + 525.0*x*y**3 - 2520*x*y*z**2) * Mj[39] + \
                (315.0*y*z**3 - z*(157.5*x**2*y + 262.5*y**3)) * Mj[40] + (-1.875*x**4 - 11.25*x**2*y**2 - 9.375*y**4 - 15.0*z**4 + z**2*(22.5*x**2 + 67.5*y**2)) * Mj[41] + \
                (105.0*x*z**3 - z*(52.5*x**3 + 157.5*x*y**2)) * Mj[42] + (26.25*x**4 - 157.5*x**2*y**2 - 393.75*y**4 + 2520*y**2*z**2 - 420*z**4) * Mj[43] + \
                (7560*x*z**3 + z*(-1890.0*x**3 - 17010.0*x*y**2)) * Mj[44] + (4725.0*x**4 + 28350.0*x**2*y**2 - 14175.0*y**4 + z**2*(-56700*x**2 + 56700*y**2)) * Mj[45] + \
                (z*(207900*x**3 - 623700*x*y**2)) * Mj[46] + (-311850*x**4 + 1871100*x**2*y**2 - 311850*y**4) * Mj[47], 

                (2) * Mj[5] + \
                (-12*y) * Mj[10] + (6*z) * Mj[11] + \
                (-12*x) * Mj[12] + (180*x*y) * Mj[17] + \
                (-60*y*z) * Mj[18] + (-6*x**2 - 6*y**2 + 12*z**2) * Mj[19] + \
                (-60*x*z) * Mj[20] + (90*x**2 - 90*y**2) * Mj[21] + \
                (-2520*x**2*y + 840*y**3) * Mj[26] + (1260*x*y*z) * Mj[27] + \
                (45.0*x**2*y + 45.0*y**3 - 180*y*z**2) * Mj[28] + (20*z**3 - 6*z*(5*x**2 + 5*y**2)) * Mj[29] + \
                (45.0*x**3 + 45.0*x*y**2 - 180*x*z**2) * Mj[30] + (6*z*(105*x**2 - 105*y**2)) * Mj[31] + \
                (-840*x**3 + 2520*x*y**2) * Mj[32] + (37800*x**3*y - 37800*x*y**3) * Mj[37] + \
                (6*z*(-3780*x**2*y + 1260*y**3)) * Mj[38] + (-840*x**3*y - 840*x*y**3 + 5040*x*y*z**2) * Mj[39] + \
                (-420*y*z**3 + 6*z*(52.5*x**2*y + 52.5*y**3)) * Mj[40] + (11.25*x**4 + 22.5*x**2*y**2 + 11.25*y**4 + 30*z**4 - 12*z**2*(7.5*x**2 + 7.5*y**2)) * Mj[41] + \
                (-420*x*z**3 + 6*z*(52.5*x**3 + 52.5*x*y**2)) * Mj[42] + (-420*x**4 + 420*y**4 + 12*z**2*(210*x**2 - 210*y**2)) * Mj[43] + \
                (6*z*(-1260*x**3 + 3780*x*y**2)) * Mj[44] + (9450*x**4 - 56700*x**2*y**2 + 9450*y**4) * Mj[45]
               ]
    else:
        raise NotImplementedError
    return np.array(grad)