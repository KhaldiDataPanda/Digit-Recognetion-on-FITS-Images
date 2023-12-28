from astropy.io import fits

# Define the paths for the three FITS files
file1_path = 'fits_file/selected_images-part1.fits'
file2_path = 'fits_file/selected_images-part2.fits'
file3_path = 'fits_file/selected_images-part3.fits'

# Open the three FITS files
hdul1 = fits.open(file1_path)
hdul2 = fits.open(file2_path)
hdul3 = fits.open(file3_path)

# Create a new HDU list to store the grouped data
grouped_hdu_list = fits.HDUList()

# Append the data from each FITS file to the new HDU list
grouped_hdu_list.append(hdul1[0])

for i in range(1, len(hdul1)):
    grouped_hdu_list.append(hdul1[i])

for i in range(1, len(hdul2)):
    grouped_hdu_list.append(hdul2[i])
    
for i in range(1, len(hdul3)):
    grouped_hdu_list.append(hdul3[i])


# Save the grouped data to a new FITS file
grouped_hdu_list.writeto('selected_image.fits')

# Close the FITS files
hdul1.close()
hdul2.close()
hdul3.close()
