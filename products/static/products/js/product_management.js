
$('#id-list-image').change(function() {
    var file = $('#id-list-image')[0].files[0];
    $('#filename').text(`Thumbnail will be set to: ${file.name}`).addClass('text-danger');
    $('#current-image').hide();
});


$('#id-brand-logo').change(function() {
    var file = $('#id-brand-logo')[0].files[0];
    $('#logo-filename').text(`Logo will be set to: ${file.name}`).addClass('text-danger');
    $('#modal-logo-thumbnail').hide();
});

$(document).ready(function() {
    var formIdx = $('#id_images-TOTAL_FORMS').val();
    $('#add-image-form').click(function() {
        // Append the new form to the formset - function suggested by ChatGPT
        var newFormHtml = $('#empty-form').html().replace(/__prefix__/g, formIdx);
        $('#formset-images').append(newFormHtml);
        
        // Increment the total forms count
        $('#id_images-TOTAL_FORMS').val(++formIdx);
        
        // Trigger the file input click event
        $('#formset-images').find('input[type="file"]').last().click();
    });
});

/******* suggested by chatGPT ******/
function openModal(modelType, action, instanceId = null) {
    const modalTitle = document.getElementById("relatedModelModalLabel");
    const modalBody = document.getElementById("relatedModelModalBody");
    const modalInstance = new bootstrap.Modal(document.getElementById('relatedModelModal'));

    // Clear previous content and event listeners
    modalBody.innerHTML = '';
    
    // Determine the URL based on action
    let url;
    if (action === "add") {
        modalTitle.textContent = `Add New ${capitalizeFirstLetter(modelType)}`;
        url = `/products/add-related-model/${modelType}/`;
    } else if (action === "edit" && instanceId) {
        modalTitle.textContent = `Edit ${capitalizeFirstLetter(modelType)}`;
        url = `/products/edit-related-model/${modelType}/${instanceId}/`;
    } else {
        console.error("Invalid action or missing instanceId");
        return;
    }

    // Fetch the form HTML
    fetch(url, {
        method: "GET",
        headers: {
            "X-Requested-With": "XMLHttpRequest"
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            modalBody.innerHTML = data.form_html;
            modalInstance.show();

            // Attach submit event handler to the form
            const modalForm = document.getElementById("relatedModelForm");
            modalForm.addEventListener('submit', function(e) {
                e.preventDefault();
                submitModalForm(modalForm);
            });

            // Attach logo change handler if needed
            attachLogoChangeHandler();
        } else {
            console.error("Failed to load form:", data.error);
        }
    })
    .catch(error => console.error("Error fetching form:", error));
}

function submitModalForm(form) {
    const formData = new FormData(form);
    fetch(form.action, {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Close the modal
            const modalInstance = bootstrap.Modal.getInstance(document.getElementById('relatedModelModal'));
            modalInstance.hide();

            // Update the select options dynamically proposed by ChatGPT
            updateSelectOptions(data.model_type, data.instance);
            selectNewOption(data.model_type, data.instance.id);

        } else {
            // Display form with errors
            document.getElementById('relatedModelModalBody').innerHTML = data.form_html;

            // Re-attach submit event handler
            const modalForm = document.getElementById("relatedModelForm");
            modalForm.addEventListener('submit', function(e) {
                e.preventDefault();
                submitModalForm(modalForm);
            });

            // Re-attach logo change handler if needed
            attachLogoChangeHandler();
        }
    })
    .catch(error => console.error('Error submitting form:', error));
}


// Helper function to capitalize the first letter
function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

function updateSelectOptions(modelType, instance) {
    const selectElement = document.getElementById(`${modelType}_select`);
    if (selectElement) {
        const existingOption = selectElement.querySelector(`option[value='${instance.id}']`);
        if (existingOption) {
            existingOption.textContent = instance.name;
        } else {
            const newOption = document.createElement('option');
            newOption.value = instance.id;
            newOption.textContent = instance.name;
            selectElement.appendChild(newOption);
        }
    }
}

function selectNewOption(modelType, instanceId) {
    const selectElement = document.getElementById(`${modelType}_select`);
    if (selectElement) {
        selectElement.value = instanceId;
    }
}

// Function to handle logo file input changes for preview
function attachLogoChangeHandler() {
    const logoInput = document.querySelector('input[name="logo"]');
    if (logoInput) {
        logoInput.addEventListener('change', function() {
            const file = logoInput.files[0];
            const logoFilename = document.getElementById('logo-filename');
            const logoThumbnail = document.getElementById('modal-logo-thumbnail');

            if (file) {
                logoFilename.textContent = `Logo will be set to: ${file.name}`;
                logoFilename.classList.add('text-danger');

                // Display a preview of the selected image
                const reader = new FileReader();
                reader.onload = function(e) {
                    logoThumbnail.src = e.target.result;
                    logoThumbnail.style.display = 'block';
                }
                reader.readAsDataURL(file);
            } else {
                logoFilename.textContent = '';
                logoFilename.classList.remove('text-danger');
                // Reset the thumbnail to the current image if available
                if (logoThumbnail.dataset.originalSrc) {
                    logoThumbnail.src = logoThumbnail.dataset.originalSrc;
                }
            }
        });
    }
}

// Function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Handle the Add Taste Categories button click
document.getElementById('add-taste-categories-button').addEventListener('click', function() {
    const formContainer = document.getElementById('add-taste-category-form');
    const formData = new FormData();
    
    // Get CSRF token
    formData.append('csrfmiddlewaretoken', getCookie('csrftoken'));

    // Get selected taste categories
    const checkboxes = formContainer.querySelectorAll('input[name="taste_categories"]:checked');
    const selectedCategories = [];
    checkboxes.forEach((checkbox) => {
        selectedCategories.push(checkbox.value);
        formData.append('taste_categories', checkbox.value);
    });

    if (selectedCategories.length === 0) {
        alert('Please select at least one taste category to add.');
        return;
    }

    // Get the URL from the data attribute
    const url = this.getAttribute('data-url');
    console.log('AJAX URL:', url);  // Debugging: Check the URL in the console

    fetch(url, {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        },
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Update the table with new taste categories
            updateTasteCategoriesTable(data.new_taste_categories);
            // Reset the form
            checkboxes.forEach((checkbox) => {
                checkbox.checked = false;
            });
            alert('Taste categories added successfully.');
        } else {
            // Display errors
            console.error('Error:', data.error);
            alert('Error adding taste categories: ' + data.error);
        }
    })
    .catch(error => console.error('Error:', error));
});

function updateTasteCategoriesTable(newCategories) {
    const tableBody = document.querySelector('#taste-categories-table tbody');
    const totalForms = document.getElementById('id_tastecategory_set-TOTAL_FORMS');
    let formIndex = parseInt(totalForms.value);

    newCategories.forEach(category => {
        const newRow = document.createElement('tr');
        newRow.innerHTML = `
            <td class="text-center">
                <div class="d-flex align-items-center">
                    <div class="rounded-circle ts-taste-icons-black text-center d-flex align-items-center justify-content-center">
                        ${category.fa_icon}
                    </div>
                    <span class="ts-taste-icon-black-text ms-2">${category.name}</span>
                </div>
                <!-- Hidden fields -->
                <input type="hidden" name="tastecategory_set-${formIndex}-taste_category" value="${category.taste_category_id}" id="id_tastecategory_set-${formIndex}-taste_category">
            </td>
            <td>
                <div class="form-check">
                    <input type="checkbox" name="tastecategory_set-${formIndex}-DELETE" id="id_tastecategory_set-${formIndex}-DELETE">
                </div>
            </td>
        `;
        tableBody.appendChild(newRow);
        formIndex++;
    });
    incrementTotalForms(newCategories.length);
}

function incrementTotalForms(number = 1) {
    const totalForms = document.getElementById('id_tastecategory_set-TOTAL_FORMS');
    totalForms.value = parseInt(totalForms.value) + number;
}
