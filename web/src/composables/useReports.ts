import api from '@/helpers/api'
import {ref} from 'vue'
import type {Report} from '@/types'

export const useReports = () => {
    const reports = ref<Report[]>([])
    const error = ref()
    const message = ref()
    const isLoadingReport = ref(false)
    const fetchReports = async () => {
        try {
            isLoadingReport.value = true
            const response = await api.get(`/analytic/reports/`)
            reports.value = response.data
        } catch (e) {
            error.value = e
        } finally {
            isLoadingReport.value = false
        }
    }

    const onUpload = async (event: any) => {
        let formData = new FormData();
        formData.append('file', event.files[0]);
        try {
            const {data} = await api.post(`/analytic/upload/`,
                formData,
                {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                    },
                })
            message.value = data.detail
            await fetchReports()
        } catch (e: any) {
            error.value = e.response.data.error
        }
    }
    return {
        reports,
        error,
        message,
        fetchReports,
        isLoadingReport,
        onUpload,
    }
}
