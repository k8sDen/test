import api from '@/helpers/api'
import {ref} from 'vue'
import type {Post} from "@/types.ts";

export const usePosts = () => {
    const error = ref()
    const posts = ref<Post[]>([])
    const isLoadingPosts = ref(false)
    const fetchPosts = async () => {
        try {
            isLoadingPosts.value = true
            const response = await api.get(`/parser/posts/`)
            posts.value = response.data
        } catch (e) {
            error.value = e
        } finally {
            isLoadingPosts.value = false
        }
    }
    return {
        posts,
        fetchPosts,
        isLoadingPosts,
    }
}
